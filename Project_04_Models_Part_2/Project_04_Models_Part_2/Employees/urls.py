from django.urls import path, include
from Project_04_Models_Part_2.Employees import views


urlpatterns = [
    # path('', views.employees_general_page),
    path('', views.employee_profile_page),

]
