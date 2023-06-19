from django.db import models

# Create your models here.

from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=30)
    department_id = models.CharField(max_length=30)
    department_philosophy_id = models.CharField(max_length=100)
    department_size = models.CharField(max_length=5)


class Employee(models.Model):
    employee_member_name = models.CharField(max_length=30)
    employee_member_position = models.CharField(max_length=30)
    employee_member_personal_id = models.CharField(max_length=2)
    employee_member_department_id = models.CharField(max_length=2)
    employee_member_languages_and_frameworks_used = models.CharField(max_length=50)
    employee_philosophy_id = models.CharField(max_length=100)
    employee_member_working_on_projects_num = models.CharField(max_length=30)
    employee_member_working_on_projects_by_name = models.CharField(max_length=30)


class Projects(models.Model):
    project_id = models.CharField(max_length=2)
    project_name = models.CharField(max_length=30)
    project_languages_and_frameworks_used = models.CharField(max_length=50)
    project_involved_departments_num = models.CharField(max_length=30)
    project_involved_departments_by_id = models.CharField(max_length=30)
    project_involved_departments_by_name = models.CharField(max_length=50)
    project_involved_employees_by_num = models.CharField(max_length=30)
    project_involved_employees_by_id = models.CharField(max_length=30)
    project_involved_employees_by_name = models.CharField(max_length=50)


class Philosophy(models.Model):
    philosophy_name = models.CharField(max_length=100)
    philosophy_id = models.CharField(max_length=100)
    philosophy_description = models.CharField(max_length=100)
    philosophy_department_following_num = models.CharField(max_length=100)
    philosophy_department_following_by_id = models.CharField(max_length=100)
    philosophy_department_following_by_name = models.CharField(max_length=100)
    philosophy_employees_following_num = models.CharField(max_length=100)
    philosophy_employees_following_by_id = models.CharField(max_length=100)
    philosophy_employees_following_by_name = models.CharField(max_length=100)









