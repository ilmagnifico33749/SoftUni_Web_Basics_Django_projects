from django.contrib import admin

# Register your models here.

from Project_04_Models_Part_2.Employees.models import Employee
from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Projects.models import Project, ProjectAppointmentDepartmentsAndEmployees


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    admin.register()
    list_display = ['employee_first_name', 'employee_last_name', 'employee_position']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_status']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_status']


@admin.register(ProjectAppointmentDepartmentsAndEmployees)
class ProjectAppointmentDepartmentsAndEmployees(admin.ModelAdmin):
    list_display = [
        'current_project_name',
        'show_all_departments_involved',
        'show_count_employees_involved',
        'show_all_employees_involved'
    ]

