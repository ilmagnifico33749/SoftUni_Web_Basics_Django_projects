from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


# Without Render
# def show_department(request: HttpRequest, *args, **kwargs):
#     print(request.method)
#     print(request.GET)
#     print(request.get_host())
#     print(request.get_port())
#     print(request.headers)
#
#     body = f'path: {request.path},args={args}, kwargs={kwargs}'
#     return HttpResponse(body)

# With Render
def show_department(request: HttpRequest, *args, **kwargs):
    context = {
        'method': request.method,
        'GET': request.GET,
        'order_by': request.GET.get('order_by', 'name')
    }

    return render(request, 'departments/all.html', context)


#
def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path}, id:"{department_id}'
    return HttpResponse(body)


def show_department_by_id(request, department_id):
    if department_id == 1:
        department_name = "Developers"
    elif department_id == 2:
        department_name = "Trainers"
    html = "<html><body><h1>" \
        "Department Name: %s, Department ID: %s" \
        "</html></body></h1>" \
        % (department_name, department_id)
    return HttpResponse(html)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # return redirect(f'/departments/?order_by={order_by}')

    # to = f'/departments/?order_by={order_by}'
    # to = 'https://softuni.bg'
    # return redirect(to)
    # return redirect('show-departments')
    return redirect('show-department-details', shodepartment_id=1)
    # ^ the above last 'Redirect' is not working property right now, to verify why later


def show_not_found(request):
    # Variant 1
    # # return HttpResponseNotFound()
    # return HttpResponseNotFound('Sorry, this page could not be found!')

    # Variant 2
    # status_code = 404
    # if status_code == 404:
    #     return HttpResponseNotFound('This page cannot be found.')
    # elif status_code == 400:
    #     return HttpResponseBadRequest('This is a bad request.')

    # Variant 3
    # status_code = 404
    # # return HttpResponse(status=status_code)
    # return HttpResponse('This page cannot be found.', status=status_code)

    # Variant 4
    # raise Http404('This page cannot be found!')

    # Variant 5 - this one is for models
    get_object_or_404()

    # pass

