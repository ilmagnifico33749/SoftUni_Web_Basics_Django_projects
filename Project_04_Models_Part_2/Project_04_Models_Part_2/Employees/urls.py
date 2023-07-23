from django.urls import path, include, re_path
from Project_04_Models_Part_2.Employees import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.employees_home_page, name='employees_home_page'),
    path('show-profile/<str:employee_user_personal_id>/<slug:slug>/', views.employee_profile_page,
         name='employee_show_profile_page'),

    path('show-employee-profile/<str:employee_user_personal_id>/', views.show_employee_user_profile, name='employee_show_user_profile'),

    path('show-all-users/', views.show_all_users_employees, name='employees_show_all_users'),
    path('create-profile/', views.employee_profile_creation, name='employee_profile_creation'),
    path('edit-profile/<str:employee_user_personal_id>/', views.employee_profile_editing, name='employee_profile_editing'),
    path('delete-profile/<str:employee_user_personal_id>/', views.employee_profile_deleting, name='employee_profile_deleting'),
    path('name_change/<str:employee_user_personal_id>/', views.employee_name_change, name='employee_name_change'),


    # re_path(r'^.*$', views.page_not_found, name='page_not_found'),
] \
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


