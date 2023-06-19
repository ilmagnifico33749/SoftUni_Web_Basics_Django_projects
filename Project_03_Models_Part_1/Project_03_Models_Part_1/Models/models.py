import datetime
from enum import Enum

from django.db import models

# Create your models here.

from django.db import models


class Department(models.Model):
    department_id = models.CharField(
        verbose_name='Department ID',
        unique=True,
        max_length=10,
        null=False,
        blank=False
    )

    department_name = models.CharField(
        verbose_name='Department name',
        unique=True,
        max_length=30,
        null=False,
        blank=False
    )

    department_employees_id = models.CharField(
        verbose_name='Employee ID',
        unique=True,
        max_length=10
    )

    department_email_address = models.EmailField(
        verbose_name='Department email address',
        unique=False,
        null=False,
        blank=False
    )

    department_project_id = models.CharField(
        verbose_name='Involved in Projects',
        unique=False,
        max_length=300,
        null=False,
        blank=False
    )


class Employee(models.Model):
    employee_id = models.CharField(
        verbose_name='Employee ID',
        unique=True,
        max_length=10,
        null=False,
        blank=False
    )

    first_name = models.CharField(
        verbose_name='First name',
        max_length=30,
        null=False,
        blank=True
    )

    last_name = models.CharField(
        verbose_name='Last name',
        max_length=40,
        null=False,
        blank=True
    )

    creation_date = models.DateTimeField(
        verbose_name='Created on',
        auto_now_add=datetime.datetime,
        null=False,
        blank=False
    )

    last_modified = models.DateTimeField(
        verbose_name='Last modified',
        auto_now=datetime.datetime,
        null=False,
        blank=False
    )

    department_name = models.CharField(
        verbose_name='Department name',
        max_length=30,
        null=False,
        blank=False
    )

    department_id = models.CharField(
        verbose_name='Department ID',
        unique=True,
        max_length=10,
        null=False,
        blank=False
    )

    project_id = models.CharField(
        verbose_name='Involved in Projects',
        unique=False,
        max_length=300,
        null=False,
        blank=False
    )

    seniority = models.CharField(
        verbose_name='Seniority',
        max_length=20
    )

    position = models.CharField(
        max_length=30
    )

    employee_email_address = models.EmailField(
        verbose_name='Employee email address',
        unique=True,
        max_length=30)

    employed_permanently = models.BooleanField(
        verbose_name='Employed permanently',
        null=True,
        blank=True,
    )
                                               # choices=(
                                               #     ('True', 'True'),
                                               #     ('False', 'False')
                                               # ))
    employed_on_probation = models.BooleanField(
        verbose_name='On probation',
        null=True,
        blank=True,
    )
                                                # choices=(
                                                #     ('True', 'True'),
                                                #     ('False', 'False')
                                                # ))
    employed_full_time = models.BooleanField(
        verbose_name='Employed full time',
        null=True,
        blank=True,
    )
                                                # choices=(
                                                #     ('True', 'True'),
                                                #     ('False', 'False')
                                                # ))
    photo = models.URLField(
        verbose_name='Photo',
        max_length=100,
        null=False,
        blank=True
    )

    birth_date = models.DateField(
        verbose_name='Birth date',
        null=False,
        blank=True
    )


class Project(models.Model):
    project_id = models.CharField(
        verbose_name='Project ID',
        unique=True,
        max_length=10,
        null=False,
        blank=True
    )

    project_name = models.CharField(
        verbose_name='Project name',
        max_length=30,
        unique=True,
        null=False,
        blank=False
    )

    project_department_id = models.CharField(
        verbose_name='Departments involved',
        max_length=300,
        unique=False,
        null=False,
        blank=True
    )

    project_employees_id = models.CharField(
        verbose_name='Employees involved',
        max_length=300,
        unique=False,
        null=False,
        blank=True
    )

    project_status = models.CharField(
        verbose_name='Project status',
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        choices=(
            ('Planing', 'Planing'),
            ('Development', 'Development'),
            ('Deployed', 'Deployed'),
            ('N/A', 'N/A')
        ),
       default='N/A'
    )

    project_email_address = models.EmailField(
        verbose_name='Project email address',
        unique=False,
        null=False,
        blank=False
    )



# TEST CLASSES FOR RELATIONS

# class Test_Department(models.Model):
#     test_department_id = models.CharField(verbose_name='TEST_Department ID', unique=True, max_length=10, null=False, blank=False)
#     test_department_name = models.CharField(verbose_name='TEST_Department name', unique=True, max_length=30, null=False, blank=False)
#     test_department_employees_id = models.CharField(verbose_name='TEST_Employee ID', unique=True, max_length=10)
#     test_department_email_address = models.EmailField(verbose_name='TEST_Department email address', unique=False, null=False, blank=False)
#     test_department_project_id = models.CharField(verbose_name='TEST_Involved in Projects', unique=False, max_length=300, null=False, blank=False)


class Test_Project(models.Model):
    test_project_id = models.CharField(
        verbose_name='TEST_Project ID',
        unique=True,
        max_length=10,
        null=False,
        blank=True
    )

    test_project_name = models.CharField(
        verbose_name='TEST_Project name',
        max_length=30,
        unique=True,
        null=False,
        blank=False
    )

    # test_project_department_id = models.CharField(verbose_name='TEST_Departments involved', max_length=300, unique=False,
    #                                          null=False, blank=True)
    test_project_employees_id = models.CharField(
        verbose_name='TEST_Employees involved',
        max_length=300,
        unique=False,
        null=False,
        blank=True
    )

    # test_project_department_appointment = models.ManyToManyField(Test_Department, through='Test_Project_Department_Appointment')


class Test_Employee(models.Model):
    test_employee_id = models.CharField(
        verbose_name='TEST_Employee ID',
        unique=True,
        max_length=10,
        null=False,
        blank=False
    )

    test_employee_full_name = models.CharField(
        verbose_name='TEST_Full name',
        max_length=30,
        null=False,
        blank=True
    )

    # test_department_id = models.ForeignKey(verbose_name='Department ID', to=Test_Department, on_delete=models.CASCADE)
    # test_project_id = models.CharField(verbose_name='Involved in Projects', to=Test_Project, on_delete=models.CASCADE)
    test_employee_project_appointment = models.ManyToManyField(
        Test_Project,
        through='Test_Project_Employees_Appointment'
    )

    # test_employee_department_appointment = models.ManyToManyField(Test_Department, through='Test_Department_Employees_Appointment')

    def __str__(self):
        return f'Test Employee ID: {self.test_employee_id} / Test Employee Full Name: {self.test_employee_full_name}'


class Test_Project_Employees_Appointment(models.Model):
    test_employee = models.ForeignKey(Test_Employee, on_delete=models.CASCADE)
    test_project = models.ForeignKey(Test_Project, on_delete=models.CASCADE)
    test_start_date = models.DateField()
    test_role = models.CharField(max_length=30)
    def __str__(self):
        return f'Test Employee: {self.test_employee} / Test Project: {self.test_project} / Test Start Date: {self.test_start_date} / Test Role: {self.test_role}'


#
# class Test_Department_Employees_Appointment(models.Model):
#     test_department_employees = models.ForeignKey(Test_Employee, on_delete=models.CASCADE)
#     test_department = models.ForeignKey(Test_Department, on_delete=models.CASCADE)
#     test_start_date = models.DateField()
#     test_role = models.CharField(max_length=30)
#


#
#
# class Test_Project_Department_Appointment(models.Model):
#     department = models.ForeignKey(
    #     Test_Department,
    #     on_delete=models.CASCADE)
    #     project = models.ForeignKey(
    #     Test_Project,
    #     on_delete=models.CASCADE)
    #     start_date = models.DateField()
    #     role = models.CharField(max_length=30)





