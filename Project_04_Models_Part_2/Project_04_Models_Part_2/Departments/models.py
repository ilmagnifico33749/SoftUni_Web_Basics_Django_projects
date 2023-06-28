import datetime

from django.db import models

# Create your models here.


class Department(models.Model):
    DEPARTMENT_STATUSES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('N/A', 'N/A'),
    ]

    # @staticmethod
    # def department_id_setting_function():
    #     count_departments = Department.objects.all().count()+1
    #     return count_departments

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

    # department_id = models.CharField(
    #     verbose_name='Department ID',
    #     max_length=10,
    #     blank=False,
    #     null=False,
    #     editable=False,
    #     default=department_id_setting_function()
    # )

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

    department_status = models.CharField(
        verbose_name='Department Status',
        max_length=10,
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=DEPARTMENT_STATUSES,
    )


    def __str__(self):
        # return f"{self.department_id}/{self.department_name}/{self.department_status}"
        # return f"{self.department_name}/{self.department_status}"
        return f"{self.department_name}"
