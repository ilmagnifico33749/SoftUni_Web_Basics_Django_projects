from django.contrib import admin
from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='photos-add'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='photos-details'),
        path('edit/', views.edit_photo, name='photos-edit'),
    ])),
]
