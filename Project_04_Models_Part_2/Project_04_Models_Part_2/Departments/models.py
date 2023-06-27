import datetime

from django.db import models

# Create your models here.


class Department(models.Model):

    @staticmethod
    def department_id_setting_function():
        count = Department.objects.all().count()+1
        return count

    department_creation_date = models.DateTimeField(
        verbose_name='Department creation date',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    department_last_modified = models.DateTimeField(
        verbose_name='Last modified on',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    department_id = models.CharField(
        verbose_name='Department ID',
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        default=department_id_setting_function()
    )

    department_name = models.CharField(
        verbose_name='Department name',
        max_length=20,
        unique=False,
        blank=False,
        null=False,
        editable=True,
    )

    department_email_address = models.EmailField(
        verbose_name='Email address',
        unique=True,
        blank=False,
        null=False,
        editable=True
    )

    projects = models.CharField(
        verbose_name='Projects',
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=
    )




