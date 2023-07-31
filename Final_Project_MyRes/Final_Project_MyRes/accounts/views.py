from Final_Project_MyRes.accounts.models import UserModel, UserProfile, RegularClientUserProfile

from django.forms import forms, TextInput, modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django import forms
from django.utils.translation import gettext_lazy as _


# class DisabledFormFieldsMixin:
#     disabled_fields = ()
#
#     def get_form(self, *args, **kwargs):
#         form = super().get_form(*args, **kwargs)
#
#         # fields = self.disabled_fields \
#         # if self.disabled_fields != '__all__' \
#         # else
#
#         for field in self.disabled_fields:
#             form.fields[field].widget.attrs['disabled'] = 'disabled'
#             # form.fields[field].widget.attrs['readonly'] = 'readonly'
#
#         return form


UserModel = get_user_model()

class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

class UserRegistrationView(generic_views.CreateView):
    form_class = RegisterUserForm
    # model = UserModel
    template_name = 'auth/user_creation.html'
    success_url = 'base/home_page.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result




    #
    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #
    #     if self.request.user.is_authenticated and self.request.user.is_staff and self.request.user.is_superuser:
    #         self.disabled_fields = (
    #             ''
    #         )
