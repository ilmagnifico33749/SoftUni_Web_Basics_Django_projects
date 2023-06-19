from django.shortcuts import render

# Create your views here.


def add_photo(request):
    return render(request=request, template_name='photos/photo-add-page.html')


def show_photo_details(request, pk):
    return render(request=request, template_name='photos/photo-details-page.html')


def edit_photo(request, pk):
    return render(request=request, template_name='photos/photo-edit-page.html')

