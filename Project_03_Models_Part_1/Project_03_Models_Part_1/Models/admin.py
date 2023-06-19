from django.contrib import admin

# Register your models here.


from Project_03_Models_Part_1.Models.models import Employee, Department, Project
# from Project_03_Models_Part_1.Models.models import Test_Project, Test_Department, Test_Employee, Test_Department_Employees_Appointment, Test_Project_Employees_Appointment
from Project_03_Models_Part_1.Models.models import Test_Project, Test_Employee, Test_Project_Employees_Appointment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name', 'department_email_address']
    list_filter = ['department_id', 'department_name']
    search_fields = ['department_id', 'department_name', 'department_email_address', 'department_employees_id', 'department_project_id']
    fieldsets = (
        ('Department Info', {'classes': ('collapse',),
                             'fields': ['department_id', 'department_name', 'department_employees_id', 'department_email_address', 'department_project_id']}),
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'last_name', 'department_name', 'project_id', 'position', 'seniority', 'employee_email_address', 'creation_date', 'last_modified']
    list_filter = ['department_name', 'position', 'seniority']
    search_fields = ['employee_id', 'first_name', 'last_name', 'project_id', 'department_name', 'project_id', 'department_employees_id', 'department_project_id']
    fieldsets = (
        ('Personal Info', {'classes': ('collapse',),
          'fields': ['employee_id', 'first_name', 'last_name', 'employee_email_address', 'photo', 'birth_date']}),
        ('Employment Contract', {'classes': ('collapse',),
          'fields': ['employed_permanently', 'employed_on_probation', 'employed_full_time']}),
        ('Employment Details', {'classes': ('collapse',),
          'fields': ['department_name', 'department_id', 'seniority', 'position']}),
        ('Projects Involvement', {'classes': ('collapse',),
          'fields': ['project_id', ]})
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'project_name', 'project_status', 'project_email_address']
    list_filter = ['project_id', 'project_name', 'project_status']
    fieldsets = (
        ('Project Info', {'classes': ('collapse',),
          'fields': ['project_id', 'project_name', 'project_status', 'project_email_address']}),
        ('Departments and Employees Involved', {'classes': ('collapse',),
          'fields': ['project_department_id', 'project_employees_id', ]}),
    )



# TEST CLASSES FOR RELATIONS
#
# @admin.register(Test_Department)
# class Test_Department(admin.ModelAdmin):
#     pass

@admin.register(Test_Project)
class Test_Project(admin.ModelAdmin):
    list_display = ['test_project_id', 'test_project_name']


@admin.register(Test_Employee)
class Test_Employee(admin.ModelAdmin):
    list_display = ['test_employee_id', 'test_employee_full_name']


# @admin.register(Test_Department_Employees_Appointment)
# class Test_Department_Employees_Appointment(admin.ModelAdmin):
#     pass

@admin.register(Test_Project_Employees_Appointment)
class Project_Employees_Appointment(admin.ModelAdmin):
    list_display = ['test_employee', 'test_project', 'test_start_date', 'test_role']







