from django import forms
from Project_04_Models_Part_2.Employees.models import Employee


class EmployeeProfileEditing(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = [
            'employee_user_personal_id',
            # 'slug'
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['employee_user_personal_id'].widget.attrs['disabled'] = True
    #     # self.fields['employee_user_personal_id'].widget.attrs['readonly'] = True




