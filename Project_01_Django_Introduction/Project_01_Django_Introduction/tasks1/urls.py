from django.urls import path, include
from Project_01_Django_Introduction.tasks1 import views

urlpatterns = [
    path('', views.index),
]












