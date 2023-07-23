from django.contrib import admin

# Register your models here.

from Project_04_Models_Part_2.Departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_status']


