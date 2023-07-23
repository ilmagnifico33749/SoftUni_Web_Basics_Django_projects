from django import forms
from Project_04_Models_Part_2.Employees.models import Employee

class EmployeeProfileDeletingConfirmation(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
