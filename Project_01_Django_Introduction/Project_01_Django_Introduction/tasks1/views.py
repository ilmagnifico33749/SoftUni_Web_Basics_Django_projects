from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from Project_01_Django_Introduction.tasks1.models import Task


def index(request):
    tasks_list = Task.objects.all()
    output = "; ".join(f"{t.task_title}: {t.task_text} - Status: {t.task_status} | Priority: {t.task_priority}" for t in tasks_list)

    if not output:
        output = "There are no created tasks1!"

    return HttpResponse(output)
