from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound


def home_page(request):
    text_info = f"Welcome to our Home page!" \
        f"\nPlease chose one of the following: \nHome \nDepartments \nSoftuni"
    b = 'Hello'
    return HttpResponse(text_info, b)


def softuni(request):
    return redirect('https://softuni.bg')


# def not_existing(request):
#     return HttpResponseNotFound('You are trying to access not existing page.')
