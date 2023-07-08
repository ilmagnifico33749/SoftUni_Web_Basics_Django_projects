from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from Project_04_Models_Part_2.Departments import views

urlpatterns = [
    path('', views.departments_general_page),

]
