from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager


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
    main_office = models.ForeignKey('MainOffice', on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'


class MainOffice(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField("Адрес", max_length=255)
    phone_number = models.CharField("Телефон", max_length=13)
    name_main_office = models.CharField(max_length=155)
    logo_min = models.ImageField(upload_to="logo", verbose_name='Лого филиала')
    short_logo_main = models.ImageField(upload_to="logo", verbose_name='Короткий логотип филиала')
    admin = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='main_branches',
        verbose_name="Админ филиала"
    )

    class Meta:
        db_table = 'main_office'
        verbose_name = 'Главный офис'
        verbose_name_plural = 'Главные офисы'
        ordering = ['name_main_office']

    def __str__(self):
        return self.name_main_office


class Branch(models.Model):
    name = models.CharField("Название филиала", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    phone_number = models.CharField("Телефон", max_length=13)
    logo = models.ImageField(upload_to="logo", verbose_name='Лого филиала')
    short_logo = models.ImageField(upload_to="logo", verbose_name='Короткий логотип филиала')
    admin = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='admin_branches',
        verbose_name="Админ филиала"
    )
    main_office = models.ForeignKey(MainOffice, on_delete=models.CASCADE, related_name='main_branches', )

    class Meta:
        db_table = 'branch'
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
        ordering = ['name']

    def __str__(self):
        return self.name