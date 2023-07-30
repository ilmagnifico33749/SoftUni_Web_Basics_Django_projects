from django.shortcuts import render

# Create your views here.
# app_auth/views.py

from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django import forms
from django.utils.translation import gettext_lazy as _



# def register_user(request):
#     pass

UserModel = get_user_model()

class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    # Example: Overriding fields params.
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password1'].help_text = 'It works'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )



class RegisterUserView(generic_views.CreateView):
    # -----------------------------------------
    # bare minimum
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # -----------------------------------------
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result



class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    # extra_context = {'title': 'longin', 'link_title': 'register'}

class LogoutUserView(auth_views.LogoutView):
    pass



UserModel = get_user_model()


class UsersListView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'
    # Example: custom login URL for only this view.
    # login_url = ...
