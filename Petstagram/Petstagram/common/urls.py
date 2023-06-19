from django.contrib import admin
from django.urls import path
from Petstagram.common import views

urlpatterns = [
    path('', views.index, name='home-page'),
]
