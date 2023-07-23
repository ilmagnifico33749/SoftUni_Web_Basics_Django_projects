from django.contrib import admin

# Register your models here.

from Project_04_Models_Part_2.Employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    admin.register()
    list_display = [
        'employee_first_name',
        'employee_last_name',
        'employee_position',
        'employee_seniority',
        'employee_department_name',
    ]
    # prepopulated_fields = {
    #     "slug":
    #         (
    #             "employee_user_personal_id",
    #             "employee_first_name",
    #             "employee_first_name"
    #         )
    # }


    list_filter = [
        'employee_position',
        'employee_seniority',
        'employee_department_name',
    ]

    search_fields = [
        'employee_first_name',
        'employee_last_name',
        'employee_position',
        'employee_seniority',
        'employee_department_name',
    ]

    fieldsets = (
        ('Personal info',
            {'fields':
                (
                  'employee_first_name',
                  'employee_last_name',
                  'employee_email_address',
                  'employee_photo',
                )
             }
         ),
        ('Employment info',
            {'fields':
                 (
                  'employee_position',
                  'employee_seniority',
                  'employee_department_name',

                 )


             }
         )
    )

