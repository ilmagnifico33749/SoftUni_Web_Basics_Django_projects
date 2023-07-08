from django.shortcuts import render
from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Employees.models import Employee
from Project_04_Models_Part_2.Projects.models import Project, ProjectAppointmentDepartmentsAndEmployees


# Create your views here.

from django.http import HttpResponse
from Project_04_Models_Part_2.Departments.models import Department


# def employees_general_page(request):
#     context = f"Welcome to Employees Page"
#     return render(request=request, context=context, template_name='employee_general_page')


# def current_employee_full_info():
#     for current_employee in Employee.objects.all():
#         return f"Employee full name: {current_employee.full_name}" \
#                f"Department: {current_employee.employee_department_name}" \
#                f"Position: {current_employee.employee_position}" \
#                f"Seniority: {current_employee.employee_seniority}" \
#                f"Contact details: {current_employee.employee_email_address}" \
#                f"Involved in Projects: {[project.project_name for project in ProjectAppointmentDepartmentsAndEmployees.objects.all() if current_employee.full_name in ProjectAppointmentDepartmentsAndEmployees.show_all_employees_involved]}"


# ---------------------------------------------------------------
# def current_employee_full_info(current_employee):
#     return f"Employee full name: {current_employee.full_name}" \
#            f"Department: {current_employee.employee_department_name}" \
#            f"Position: {current_employee.employee_position}" \
#            f"Seniority: {current_employee.employee_seniority}" \
#            f"Contact details: {current_employee.employee_email_address}" \
#            f"Involved in Projects: {[project.project_name for project in ProjectAppointmentDepartmentsAndEmployees.objects.all() if current_employee.full_name in ProjectAppointmentDepartmentsAndEmployees.show_all_employees_involved]}"
#
#
# def employee_profile_page(request):
#     all_employees_general_info = Employee.objects.all()
#     projects_appointments_all_info = ProjectAppointmentDepartmentsAndEmployees.objects.all()
#     # context = {
#     #     'all_employees_general_info': all_employees_general_info,
#     #     'projects_appointments_all_info': projects_appointments_all_info,
#     # }
#     # context = {current_employee_full_info}
#     context = {'all_employees_general_info': all_employees_general_info,
#         'Employee full name': Employee.full_name,
#         'Department': Employee.employee_department_name,
#         'Position': Employee.employee_position,
#         'Seniority': Employee.employee_seniority,
#         'Contact details': Employee.employee_email_address,
#         'Involved in projects': '\n'.join([project.project_name for project in projects_appointments_all_info if Employee.full_name in project.show_all_employees_involved()]),
#         'function_current_employee_full_info': current_employee_full_info,
#     }
#     return render(request=request, template_name='Employees/employee_profile_page.html', context=context)
# ---------------------------------------------------------------

def employee_project_appointment(current_employee: Employee):
    all_projects_appointed = []
    for project in ProjectAppointmentDepartmentsAndEmployees.objects.all():
        if current_employee.full_name in project.show_all_employees_involved():
            all_projects_appointed.append(str(project.current_project_name))
    return f"{', '.join(all_projects_appointed)}"
    # return all_projects_appointed


def employee_profile_page(request):
    all_employees = Employee.objects.all()
    all_employees_info = []
    for employee in all_employees:
        current_employee_info = {
            'Employee full name': employee.full_name,
            'Department': employee.employee_department_name,
            'Position': employee.employee_position,
            'Seniority': employee.employee_seniority,
            'Contact details': employee.employee_email_address,
            'Appointed to Projects': employee_project_appointment(employee)
        }
        all_employees_info.append(current_employee_info)
    context = {'all_employees_info': all_employees_info,}
    return render(request=request, template_name='Employees/employee_profile_page.html', context=context)


