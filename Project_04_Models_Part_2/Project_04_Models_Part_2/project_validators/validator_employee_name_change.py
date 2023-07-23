from django.forms import forms


def validator_employee_name_change_different(current_first_name, new_first_name, current_last_name, new_last_name):
    if current_first_name == new_first_name and current_last_name == new_last_name:
        raise forms.ValidationError("The new name must be different than the current one.")
