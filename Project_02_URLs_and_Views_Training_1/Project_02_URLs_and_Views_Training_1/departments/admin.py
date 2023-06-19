from django.contrib import admin

# Register your models here.

from Project_02_URLs_and_Views_Training_1.departments import models

admin.site.register(models.Department)
admin.site.register(models.Employee)
admin.site.register(models.Projects)
admin.site.register(models.Philosophy)


