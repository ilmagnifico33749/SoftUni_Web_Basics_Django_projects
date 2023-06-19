from django.contrib import admin
from django.urls import path, include
from Petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='pets-add'),
    path('<slug:pet_name>/', include([
        path('', views.show_pet_details, name='pets-details'),
        path('edit/', views.edit_pet, name='pets-edit'),
        path('delete/', views.delete_pet, name='pets-delete')
    ]))
]
