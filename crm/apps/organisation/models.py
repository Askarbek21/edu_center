from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from apps.users.models import CustomUser


class Organisation(TenantMixin):
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


class Domain(DomainMixin):
    pass