from django import forms
from Project_04_Models_Part_2.project_validators.validator_employee_name_change import validator_employee_name_change_different

class EmployeeNameChangeForm(forms.Form):
    employee_new_first_name = forms.CharField(
        label='Employee New First Name',
        max_length=30,
    )
    employee_new_last_name = forms.CharField(
        label='Employee New Last Name',
        max_length=30,
    )

    def clean(self):
        cleaned_data = super().clean()
        new_first_name = cleaned_data.get('employee_new_first_name')
        new_last_name = cleaned_data.get('employee_new_last_name')

        current_first_name = self.employee_instance.employee_first_name
        current_last_name = self.employee_instance.employee_last_name

        # Validate if new names are different from the current names
        validator_employee_name_change_different(current_first_name, new_first_name, current_last_name, new_last_name)

        return cleaned_data
