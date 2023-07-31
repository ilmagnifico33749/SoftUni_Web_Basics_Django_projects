from django.urls import path
from Final_Project_MyRes.accounts.views import UserRegistrationView

urlpatterns = (
    path('create_user/', UserRegistrationView.as_view(), name='user_registration'),

)
