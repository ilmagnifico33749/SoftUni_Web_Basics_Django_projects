from django.contrib import admin

# Register your models here.

from Project_04_Models_Part_2.Projects.models import Project, ProjectAppointmentDepartmentsAndEmployees


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

