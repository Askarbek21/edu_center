from django.db import models
from django.utils import timezone

from apps.organisation.models import Organisation
from apps.tariff.models import Tariff


class License(models.Model):
    """Лицензия"""
    number_of_licenses = models.CharField(max_length=50)  # Номер договора
    created_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, related_name='tariff_license')
    status = models.BooleanField(default=False)
    organization = models.ForeignKey(Organisation, on_delete=models.DO_NOTHING, related_name='organization_license')
    price = models.IntegerField(default=0)  # Цена для оплаты

    class Meta:
        db_table = 'license'
        verbose_name = 'Лицензия'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.number_of_licenses
