from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return None
    return render(request=request, template_name='common/home-page.html')


