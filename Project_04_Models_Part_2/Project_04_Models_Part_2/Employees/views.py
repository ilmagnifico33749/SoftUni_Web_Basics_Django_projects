from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Employees.models import Employee
from Project_04_Models_Part_2.Projects.models import Project, ProjectAppointmentDepartmentsAndEmployees

from Project_04_Models_Part_2.Employees.forms.form_employee_profile_creation import EmployeeProfileCreation
from Project_04_Models_Part_2.Employees.forms.form_employee_profile_editing import EmployeeProfileEditing
from Project_04_Models_Part_2.Employees.forms.form_employee_profile_deleting_confirmation import EmployeeProfileDeletingConfirmation
from Project_04_Models_Part_2.Employees.forms.form_employee_name_change import EmployeeNameChangeForm

# Create your views here.

from django.http import HttpResponse
from Project_04_Models_Part_2.Departments.models import Department

def employees_home_page(request):
    context = {}
    return render(request=request, template_name='Employees/employees_home_page.html', context=context)

def employee_project_appointment(current_employee: Employee):
    all_projects_appointed = []
    for project in ProjectAppointmentDepartmentsAndEmployees.objects.all():
        if current_employee.full_name in project.show_all_employees_involved():
            all_projects_appointed.append(str(project.current_project_name))
    return f"{', '.join(all_projects_appointed)}"
    # return all_projects_appointed


def employee_profile_page(request, employee_user_personal_id, slug):
    current_employee = get_object_or_404(
        Employee,
        employee_user_personal_id=employee_user_personal_id,
        slug=slug
    )

    current_employee_info = {
        'Employee_full_name': current_employee.full_name,
        'Department': current_employee.employee_department_name,
        'Position': current_employee.employee_position,
        'Seniority': current_employee.employee_seniority,
        'Contact_details': current_employee.employee_email_address,
        'Appointed_to_Projects': employee_project_appointment(current_employee),
        'Employee_is_Admin': current_employee.employee_user_is_admin,
        'Employee_has_Admin Access': current_employee.employee_user_admin_access,
        'Employee_user_personal_ID': current_employee.employee_user_personal_id,
        'Employee_Slug': current_employee.slug,
        'Employee_absolute_URL': current_employee.get_absolute_url(),
        'Employee_photo': current_employee.employee_photo,

    }
    context = {'current_employee_info': current_employee_info, }
    print(f"Slug value: {slug}")
    return render(request=request, template_name='Employees/employee_show_profile_page.html', context=context)


def show_employee_user_profile(request, employee_user_personal_id):

    # all_employees = Employee.objects.all()
    # for employee in all_employees:
    #     if employee.employee_user_personal_id == employee_user_personal_id:
    #         current_employee = employee
    #         context = {'Employee_name': current_employee.full_name}

    current_employee = get_object_or_404(Employee, employee_user_personal_id=employee_user_personal_id)
    # context = {'Employee_name': current_employee.full_name}

    current_employee_info = {
        'Employee_full_name': current_employee.full_name,
        'Department': current_employee.employee_department_name,
        'Position': current_employee.employee_position,
        'Seniority': current_employee.employee_seniority,
        'Contact_details': current_employee.employee_email_address,
        'Appointed_to_Projects': employee_project_appointment(current_employee),
        'Employee_is_Admin': current_employee.employee_user_is_admin,
        'Employee_has_Admin_Access': current_employee.employee_user_admin_access,
        'Employee_user_personal_ID': current_employee.employee_user_personal_id,
        'Employee_photo': current_employee.employee_photo,
    }
    context = {'current_employee_info': current_employee_info}

    return render(request=request, template_name='Employees/employee_show_profile_page.html', context=context)


def show_all_users_employees(request):
    all_employees = Employee.objects.all()
    all_employees_info = []
    for employee in all_employees:
        current_employee_info = {
            'Employee_full_name': employee.full_name,
            'Department': employee.employee_department_name,
            'Position': employee.employee_position,
            'Employee_slug': employee.slug,
            'Employee_user_personal_ID': employee.employee_user_personal_id,
            'Employee_absolute_URL': employee.get_absolute_url(),
            # 'Employee_photo': employee.employee_photo,
        }
        all_employees_info.append(current_employee_info)
    context = {'all_employees_info': all_employees_info, }
    return render(request=request, template_name='Employees/employees_show_all_users.html', context=context)


def employee_profile_creation(request):
    if request.method == "GET":
        form = EmployeeProfileCreation()

    if request.method == "POST":
        form = EmployeeProfileCreation(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(to='http://127.0.0.1:8000/employees/')
            success_message = 'Congratulations! The profile is created!'
            return render(request, 'Employees/employee_profile_creation_success.html', {'success_message': success_message})
    else:
        form = EmployeeProfileCreation

    return render(request, 'Employees/employee_profile_creation.html', {'form': form})


def employee_profile_editing(request, employee_user_personal_id):
    instance = get_object_or_404(Employee, employee_user_personal_id=employee_user_personal_id)
    current_employee_absolute_url = instance.get_absolute_url()
    print(current_employee_absolute_url)
    if request.method == "GET":
        form = EmployeeProfileEditing(instance=instance)

    elif request.method == "POST":
        form = EmployeeProfileEditing(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            instance.refresh_from_db()

            if instance.employee_user_personal_id is None:
                instance.employee_user_personal_id = instance.employee_custom_id()
                instance.save()

            success_message = "The profile is updated successfully!"
            latest_updated_form = EmployeeProfileEditing(instance=instance)
            return render(
                request=request,
                template_name='Employees/employee_profile_editing_success.html',
                context={
                    'success_message': success_message,
                    'form': latest_updated_form,
                    'employee_absolute_url': current_employee_absolute_url
                }
            )

        else:
            fail_message = "The profile could not be updated!"
            return render(
                request=request,
                template_name='Employees/employee_profile_editing_fail.html',
                context={
                    'fail_message': fail_message,
                    'employee_id': employee_user_personal_id,
                    'form': form,
                    'employee_absolute_url': current_employee_absolute_url
                }
            )
    else:
        return HttpResponse("Invalid request method")

    return render(request, 'Employees/employee_profile_editing.html',
                  {'form': form, 'employee_absolute_url': current_employee_absolute_url})
    # return render(request, 'Employees/employee_profile_test_page.html.html', {'form': form})



def employee_profile_deleting(request, employee_user_personal_id):
    employee_to_delete = get_object_or_404(Employee, employee_user_personal_id=employee_user_personal_id)

    context = {
        'employee_user_personal_id': employee_user_personal_id,
        'Employee_name': employee_to_delete.full_name,
    }

    if request.method == "POST":
        employee_to_delete.delete()
        return render(
            request=request,
            template_name='Employees/employee_profile_deleting_success.html',
            context=context,
        )

    return render(request=request, template_name='Employees/employee_profile_deleting.html', context=context)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def employee_name_change(request, employee_user_personal_id):
    employee_to_update = get_object_or_404(Employee, employee_user_personal_id=employee_user_personal_id)
    # The below 'EmployeeNameChangeForm(request.POST)' saves the data entered in the form.
    # If you overwrite the form parameter in the way 'form = EmployeeNameChangeForm(request.POST)'
    # you will get a base form without any data
    form = EmployeeNameChangeForm(request.POST)
    context = {'employee_current_first_name': employee_to_update.employee_first_name,
               'employee_current_last_name': employee_to_update.employee_last_name,
               'employee_user_personal_id': employee_user_personal_id,
               'form': form,
               }
    form.employee_instance = employee_to_update


    if request.method == 'POST':
        form.employee_instance = employee_to_update
        if form.is_valid():
            employee_to_update.employee_first_name = form.cleaned_data['employee_new_first_name']
            employee_to_update.employee_last_name = form.cleaned_data['employee_new_last_name']
            employee_to_update.save()
            context['employee_new_first_name'] = employee_to_update.employee_first_name
            context['employee_new_last_name'] = employee_to_update.employee_last_name
            success_message = 'The employee names are changed successfully!'
            context['success_message'] = success_message
            form = EmployeeNameChangeForm()
            context['form'] = form
            return render(request=request, template_name='Employees/employee_name_change_success.html', context=context)

        else:
            fail_message = 'The employee names could not be changed!'
            context['fail_message'] = fail_message
            return render(request=request, template_name='Employees/employee_name_change_fail.html', context=context)

    return render(request=request, template_name='Employees/employee_name_change.html', context=context)
