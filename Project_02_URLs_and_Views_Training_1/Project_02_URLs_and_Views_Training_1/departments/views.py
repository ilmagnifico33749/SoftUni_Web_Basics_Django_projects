from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from Project_02_URLs_and_Views_Training_1.departments.models import Department
# from Project_02_URLs_and_Views_Training_1.departments.models import Employee
# from Project_02_URLs_and_Views_Training_1.departments.models import Project
# from Project_02_URLs_and_Views_Training_1.departments.models import Philosophy


def home(request):
    text_info = f"Welcome to our Departments page!"
    return HttpResponse(text_info)

def departments_by_id(request, department_id):
    text_info = str()
    if department_id == 1:
        text_info = f"Welcome to our Department No. {department_id} - Developers" \
                    f"\nTeam" \
                    f"\nProjects" \
                    f"\nPhilosophy"
    elif department_id == 2:
        text_info = f"Welcome to our Department No. {department_id} - R&D" \
                    f"\nTeam" \
                    f"\nProjects" \
                    f"\nPhilosophy"
    elif department_id == 3:
        text_info = f"Welcome to our Department No. {department_id} - DevOps" \
                    f"\nTeam" \
                    f"\nProjects" \
                    f"\nPhilosophy"
    else:
        # text_info = f"You are trying to access a still not existing department."
        return HttpResponseNotFound('\nYou are trying to access not existing page.')

    return HttpResponse(text_info)

    # if department_id == 1:
    #     department_name = "Developers"
    # elif department_id == 2:
    #     department_name = "Trainers"
    # html = "<html><body><h1>" \
    #     "Department Name: %s, Department ID: %s" \
    #     "</html></body></h1>" \
    #     % (department_name, department_id)
    # return HttpResponse(html)


def test_render(request):
    context = {"Programming_Language": "Python", "Framework": "Django", "Database": "PosgreSQL"}

    return render(request=request, template_name='departments/test_render.html', context=context)

def overview(request):
    department_all_info = Department.objects.all()
    context = {'department_all_info': department_all_info}
    return render(request=request, template_name='departments/departments_overview.html', context=context)
