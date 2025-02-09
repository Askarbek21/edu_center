from django.db import models
from django.contrib.auth.models import (
AbstractUser, Group, Permission, BaseUserManager
)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Super admin', 'Super Admin'),
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    username = models.CharField(max_length=64,blank=True)
    phone_number = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=64)
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_set', blank=True)
    organisation = models.ForeignKey('organisation.Organisation', on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey('branches.Branch', on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

