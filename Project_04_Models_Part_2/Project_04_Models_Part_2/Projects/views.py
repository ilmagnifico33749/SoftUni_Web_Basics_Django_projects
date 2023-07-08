from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from Project_04_Models_Part_2.Departments.models import Department


def projects_general_page(request):
    context = f"Welcome to Projects Page"
    return HttpResponse(context)
