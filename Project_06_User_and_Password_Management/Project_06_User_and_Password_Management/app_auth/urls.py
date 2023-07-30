from django.contrib import admin
from django.urls import path, include

# app_auth/urls.py

from Project_06_User_and_Password_Management.app_auth.views \
    import RegisterUserView, LoginUserView, LogoutUserView, UsersListView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UsersListView.as_view(), name='users_list'),


)

#   user: doncho
#   pass: m1nk0v$!


