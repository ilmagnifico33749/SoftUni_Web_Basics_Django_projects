from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Projects.models import ProjectAppointmentDepartmentsAndEmployees
from Project_04_Models_Part_2.Employees.models import Employee

#
#     {% for department in all_departments %}
#         <h1>{{ department.department_name }}</h1>
#         <h3>Email address: {{ department.department_email_address }}</h3>
# {#        <p>Email address: {{ department.department_email_address }}</p>#}
#         <h3>Department Details</h3>
#         <p>Department Status: {{ department.department_status }}</p>
#         <p>Department creation date: {{ department.department_creation_date }}</p>
#         <p>Department last update date: {{ department.department_last_modified }}</p>
#         <h3>Department Appointments: </h3>
#             {% for current_project in projects_appointments %}
#                 {% if department.department_name in current_project.show_all_departments_involved %}
#                     <p> - Appointed to project: {{ current_project.show_project_name }}</p>
#                     {% for employee_appointed in current_project.show_all_employees_involved %}
#                         {% for employee in all_employees_info %}
#                             {% if employee.full_name == employee_appointed %}
#                                 <p>* Department Employees Appointed: {{ employee.full_name }}</p>
#                             {% endif %}
#                         {% endfor %}
#                     {% endfor %}
#                 {% endif %}
#             {% endfor %}

def department_appointment_to_projects(department: Department):
    appointed_to_projects = []
    for project in ProjectAppointmentDepartmentsAndEmployees.objects.all():
        if department.department_name in project.show_all_departments_involved():
            appointed_to_projects.append(str(project.current_project_name))
    return f"{', '.join(appointed_to_projects)}"


def departments_general_page(request):
    all_departments = Department.objects.all()
    # projects_appointments = ProjectAppointmentDepartmentsAndEmployees.objects.all()
    # all_employees_info = Employee.objects.all()
    # project_appointment_by_department_name = [project_app_info.current_project_name for project_app_info in
    #                                           projects_appointments]

    all_departments = Department.objects.all()
    all_departments_general_info = []
    for department in all_departments:
        current_department_info = {
            'Department name': department.department_name,
            'Contact details': department.department_email_address,
            'Department status': department.department_status,
            'Department creation date': department.department_creation_date,
            'Department last update date': department.department_last_modified,
            'Department appointment to Projects': department_appointment_to_projects(department)
        }
        all_departments_general_info.append(current_department_info)

    context = {'all_departments_general_info': all_departments_general_info}

    # context = {: all_departments,
    #            'projects_appointments': projects_appointments,
    #            'all_employees_info': all_employees_info,
    #            }

    return render(request=request, template_name='Departments/departments_general_page.html', context=context)
