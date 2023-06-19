from django import shortcuts
from django.urls import path
# from Project_02_URLs_and_Views.departments import views
from Project_02_URLs_and_Views.Project_02_URLs_and_Views.departments import views


urlpatterns = [
    path('', views.show_department, name='show-departments'),
    # path('<department_id>/', views.show_department_details),
    # path('<int:department_id>/', views.show_department_details),


    # path('<department_id>/', views.show_department_by_id),
    # path('<int:department_id>/', views.show_department_by_id),
    path('<int:department_id>/', views.show_department_details, name='show-department-details'),

    path(
        '<int:department_id>/',
        views.show_department_by_id,
        name='show-department-by-id'),

    path('redirect/', views.redirect_to_first_department, name='id'),

    path('not-found/', views.show_not_found, name='not-found')

]