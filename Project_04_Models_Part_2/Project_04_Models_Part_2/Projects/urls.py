from django.urls import path, include
from Project_04_Models_Part_2.Projects import views

urlpatterns = [
    path('', views.projects_general_page),
]
