from django import forms
from Project_04_Models_Part_2.Employees.models import Employee

from django.core import validators



class EmployeeProfileCreation(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        exclude = [
            'employee_user_personal_id',
            'slug'
        ]


