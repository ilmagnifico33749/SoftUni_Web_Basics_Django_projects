from django.contrib import admin
from django.urls import path, include
from Project_02_URLs_and_Views_Training_1.departments import views

urlpatterns = (
    path('', views.home),
    path('<int:department_id>/', views.departments_by_id),
    path('test_render', views.test_render),
    path('overview', views.overview),


)
