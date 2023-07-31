from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth.models import Group, Permission
from django.core import validators as built_in_validators
from django.db.models.signals import post_save
from django.dispatch import receiver

from Final_Project_MyRes.common import user_profile_registration_required_info


class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please enter a valid email")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'email'
    USER_TYPES = (
        ('regular_client_user', 'Client'),
        ('hotel_host_user', 'Hotel Host'),
    )

    objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        null=True,
        blank=True
    )


UserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )


class RegularClientUserProfile(UserProfile):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'LGBTIQA+'),
        ('wont_say', "I don't want to say"),
    )

    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        editable=True,
    )

    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        editable=True,
    )

    phone_code = models.CharField(
        max_length=3,
        choices=user_profile_registration_required_info.all_countries_with_phone_codes_choices_fields_format
    )

    phone_number = models.CharField(
        max_length=12,
    )

    date_of_birth = models.DateField(
    )

    nationality = models.CharField(
        max_length=33,
        choices=user_profile_registration_required_info.all_countries_choices_fields_format
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDERS,
        editable=True
    )

    user_email_address_validated = models.BooleanField(
        default=False
    )

    profile_creation_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )

    profile_last_updated_date = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    profile_user_photo = models.ImageField(
        null=True,
        blank=True,
    )

