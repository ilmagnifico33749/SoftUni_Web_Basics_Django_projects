import datetime
import os
import random
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from Project_04_Models_Part_2.Departments.models import Department
from Project_04_Models_Part_2.project_validators import validator_employee_user_id

# Create your models here.

def get_upload_path(instance, filename):
    folder_name = f"{instance.employee_user_personal_id}-{instance.slug}"
    upload_dir = os.path.join("employee_user_photos", folder_name)

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    return os.path.join(upload_dir, filename)


class Employee(models.Model):
    EMPLOYEE_SENIORITY = (
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Regular', 'Regular'),
        ('Senior', 'Senior'),
    )

    EMPLOYEE_POSITION = (
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
    )

    EMPLOYEE_CONTRACTS = (
            ('Trial period', 'Trial period'),
            ('Temporary', 'Temporary'),
            ('Permanent', 'Permanent'),
            ('Terminated', 'Terminated'),
        )


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
        choices=EMPLOYEE_POSITION
    )

    employee_email_address = models.EmailField(
        verbose_name='Email address',
        unique=True,
        blank=True,
        null=True,
        editable=True
    )

    employee_contract_type = models.CharField(
        verbose_name='Contract type',
        unique=False,
        blank=False,
        null=False,
        editable=True,
        choices=EMPLOYEE_CONTRACTS
    )


    employee_user_is_admin = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        editable=True,
        choices=[
            (True, 'Yes'),
            (False, 'No'),
        ]
    )

    employee_user_admin_access = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        editable=True,
        choices=[
            (True, 'Yes'),
            (False, 'No'),
        ],

    )

    employee_user_personal_id = models.CharField(
        max_length=6,
        blank=False,
        null=True,
        unique=True,
        editable=False,
        default=None,
    )

    slug = models.SlugField(
        unique=False,
        editable=True,
        default=None,
    )


    employee_photo = models.ImageField(
        verbose_name='Employee photo',
        unique=False,
        blank=True,
        null=True,
        editable=True,
        # upload_to='employee_user_photos',
        # upload_to=f"{Employee.employee_user_personal_id}/{Employee.slug}",
        upload_to=lambda instance, filename: get_upload_path(instance, filename),
    )


    # FK

    employee_department_name = models.ForeignKey(
        to=Department,
        on_delete=models.SET_NULL,
        null=True
    )


    @property
    def full_name(self):
        return f"{self.employee_first_name} {self.employee_last_name}"

    def save(self, *args, **kwargs):
        if not self.employee_user_personal_id or self.employee_user_personal_id is None:
            self.employee_user_personal_id = self.employee_custom_id()
        if not self.slug or self.slug is None:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def employee_custom_id(self):
        all_employee_user_personal_id = [employee.employee_user_personal_id for employee in Employee.objects.all() if
                                 Employee.objects.all()]

        def random_id_generator():
            random_id = f'E{random.randint(10000, 99999)}'
            return random_id

        def id_validator(current_id, all_ids):
            if current_id in all_employee_user_personal_id or not current_id:
                print(f'{current_id} is invalid - it already exists or is empty!')
                current_id = random_id_generator()
                return id_validator(current_id, all_ids)
            else:
                return current_id

        return id_validator(random_id_generator(), all_employee_user_personal_id)

    def get_absolute_url(self):
         employee_absolute_url = reverse(
            'employee_show_profile_page',
            kwargs={
                'employee_user_personal_id': self.employee_user_personal_id,
                'slug': self.slug
            }
        )
         return employee_absolute_url




    def __str__(self):
        # return f"{self.full_name}/{self.department_name}/{self.employee_position}/{self.employee_id}"
        # return f"{self.full_name}/{self.department_name}/{self.employee_position}"
        return f"{self.full_name} - {self.employee_position}"

class EmployeePhoto(models.Model):
    employee_photo = models.ImageField(upload_to='employee_user_photos')
