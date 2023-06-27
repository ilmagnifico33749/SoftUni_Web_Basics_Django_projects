import datetime

from django.db import models
from Project_04_Models_Part_2.Departments.models import Department

import Project_04_Models_Part_2.Departments.models


# Create your models here.



class Employee(models.Model):
    EMPLOYEE_SENIORITY = [
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Regular', 'Regular'),
        ('Senior', 'Senior'),
    ]

    EMPLOYEE_POSITION = [
        ('Customer Service Rep', 'Customer Service Representative'),
        ('Tech Support Rep', 'Technical Support Representative'),
        ('Sales Rep', 'Sales Representative'),
        ('COR', 'Contracting Officer Representative'),
        ('Dev', 'Developer'),
        ('QA', 'Quality Assurance'),
        ('DevOps', 'Development and Operations Representative'),
        ('SysAdmin', 'System Administrator'),
        ('System Architect', 'System Architect'),
        ('Team Leader', 'Team Leader'),
        ('COO', 'Chief Operations Officer'),
        ('CSO', 'Chief Sales Officer'),
        ('CTO', 'Chief Technology Officer '),
        ('CPO', 'Chief Procurement Officer'),
        ('CEO', 'Chief Executive Officer')
    ]

    @staticmethod
    def employee_id_setting_function():
        count = Employee.objects.all().count()+1
        return count

    @staticmethod
    def get_department_id():
        department_id_obtainer = [department.department_id for department in Department.objects.all() if department.department_name == Employee.department_name]
        return department_id_obtainer

    employee_creation_date = models.DateTimeField(
        verbose_name='User creation date',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    employee_last_modified = models.DateTimeField(
        verbose_name='Last modified on',
        auto_now_add=datetime.datetime,
        blank=False,
        null=False,
        editable=False,
    )

    employee_id = models.CharField(
        verbose_name='Employee ID',
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        default=employee_id_setting_function(),
    )

    department_name = models.CharField(
        verbose_name='Department name',
        max_length=20,
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=Department.department_name,
    )

    department_id = models.CharField(
        verbose_name='Department ID',
        max_length=10,
        unique=False,
        blank=False,
        null=False,
        default=get_department_id()
    )

    employee_first_name = models.CharField(
        verbose_name='First name',
        max_length=30,
        unique=False,
        blank=False,
        null=False,
        editable=True
    )

    employee_last_name = models.CharField(
        verbose_name='Last name',
        max_length=30,
        unique=False,
        blank=False,
        null=False,
        editable=True
    )

    employee_seniority = models.CharField(
        verbose_name='Seniority',
        max_length=30,
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=EMPLOYEE_SENIORITY
    )

    employee_position = models.CharField(
        verbose_name='Position',
        max_length=30,
        unique=False,
        blank=False,
        null=False,
        choices= EMPLOYEE_POSITION
    )

    employee_email_address = models.EmailField(
        verbose_name='Email address',
        unique=True,
        blank=False,
        null=False,
        editable=True
    )

    employee_contract_type = models.CharField(
        verbose_name='Contract type',
        unique=False,
        blank=False,
        null=False,
        editable=True,
    )

    def full_name(self):
        return f"{self.employee_first_name} {self.employee_last_name}"

    def __str__(self):
        return f"{self.full_name()}/{self.department_name}/{self.employee_position}/{self.employee_id}"
