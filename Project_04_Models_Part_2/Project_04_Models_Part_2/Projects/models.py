import datetime

from django.db import models

from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Employees.models import Employee
# Create your models here.

class Project(models.Model):

    @staticmethod
    def project_id_setting_function():
        count = Project.objects.all().count() + 1
        return count

    project_creation_date = models.DateTimeField(
        verbose_name='Department creation date',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    project_last_modified = models.DateTimeField(
        verbose_name='Last modified on',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    project_id = models.CharField(
        verbose_name='Department ID',
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        default=project_id_setting_function(),
    )

    project_name = models.CharField(
        verbose_name='Department name',
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        editable=True,
    )

    project_address = models.EmailField(
        verbose_name='Email address',
        unique=True,
        blank=False,
        null=False,
        editable=True
    )

    project_departments_involved_id = models.CharField(
        verbose_name='Departments involved',
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=Department.department_id,
    )

    project_employees_involved_id = models.CharField(
        verbose_name='Employees involved',
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=Employee.employee_id,
    )

    project_development_start_date = models.DateTimeField(
        verbose_name='Project Development Start Date',
        unique=False,
        blank=True,
        null=False,
        auto_now=datetime.datetime
    )

    project_development_completion_deadline_date = models.DateTimeField(
        verbose_name='Project Development Completion Deadline Date',
        unique=False,
        blank=True,
        null=False,
        auto_now=datetime.datetime
    )

    project_de_start_date = models.DateTimeField(
        verbose_name='Project Development Start Date',
        unique=False,
        blank=True,
        null=False,
        auto_now=datetime.datetime
    )
