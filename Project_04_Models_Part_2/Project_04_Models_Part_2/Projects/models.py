import datetime

from django.db import models

from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.Employees.models import Employee
# Create your models here.

class Project(models.Model):
    PROJECT_STATUSES = [
            ('N/A', 'N/A'),
            ('Planing', 'Planing'),
            ('Development', 'Development'),
            ('Deployment', 'Deployment'),
            ('Termination', 'Termination'),
    ]

    # @staticmethod
    # def project_id_setting_function():
    #     projects_count = Project.objects.all().count() + 1
    #     return projects_count

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

    # project_id = models.CharField(
    #     verbose_name='Department ID',
    #     max_length=10,
    #     blank=False,
    #     null=False,
    #     editable=False,
    #     default=project_id_setting_function(),
    # )

    project_name = models.CharField(
        verbose_name='Project name',
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        editable=True,
    )

    project_email_address = models.EmailField(
        verbose_name='Email address',
        unique=True,
        blank=False,
        null=False,
        editable=True
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

    project_status = models.CharField(
        verbose_name='Project Status',
        max_length=20,
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=PROJECT_STATUSES
    )

    project_deployment_start_date = models.DateTimeField(
        verbose_name='Project Development Start Date',
        unique=False,
        blank=True,
        null=False,
        auto_now=datetime.datetime
    )

    # FK

    # project_departments_appointed = models.ManyToManyField(
    #     Department,
    #     through='ProjectAppointmentDepartmentsAndEmployees',
    # )

    # project_employees_appointed = models.ManyToManyField(Employee, through='ProjectAppointmentDepartmentsAndEmployees')



    def __str__(self):
        # return f"{Project.project_id}/{Project.project_name}/{Project.project_status}"
        # return f"{Project.project_name}/{Project.project_status}"
        return f"{self.project_name}/{self.project_status}"

class ProjectAppointmentDepartmentsAndEmployees(models.Model):
    current_project_name = models.ForeignKey(Project, on_delete=models.RESTRICT)
    # project_appointed_departments = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    # project_appointed_employees = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    project_appointed_departments = models.ManyToManyField(Department)
    project_appointed_employees = models.ManyToManyField(Employee)

    def show_all_departments_involved(self):
        return [department.department_name for department in self.project_appointed_departments.all()]

    def show_count_employees_involved(self):
        return [self.project_appointed_employees.count()]

    def show_all_employees_involved(self):
        return [employee.full_name() for employee in self.project_appointed_employees.all()]
