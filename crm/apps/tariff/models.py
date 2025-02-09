from enum import Enum

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TariffOptionCode(Enum):
    """код Студент, Учитель и т.д (это просто пример)"""
    STUDENT = 'student'

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name) for tag in cls]


class TariffOptionCodeName(models.Model):
    """Тут теперь название кода. Например: для код студент:Название Студент и т.д)"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, choices=TariffOptionCode.choices(), unique=True)

    class Meta:
        db_table = 'tariff_option_code_name'
        verbose_name = 'Tariff Option Code'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TariffType(models.Model):
    """Пример: Стандарт, Про, Премиум, ... """
    name = models.CharField(max_length=100)
    price_monthly = models.IntegerField()
    price_yearly = models.IntegerField()
    is_demo = models.BooleanField(default=False)
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], default=3)

    class Meta:
        db_table = 'tariff_type'
        verbose_name = 'Tariff Type'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tariff(models.Model):
    """УЖе тут должно быть название тарифа, например: Кол-во студентов == 8, Кол-во учителей=10 (Это просто пример)"""
    name = models.CharField(max_length=199)
    value = models.IntegerField()
    tariff_type = models.ForeignKey(TariffType, on_delete=models.CASCADE)
    tariff_code = models.ForeignKey(TariffOptionCodeName, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tariff'
        verbose_name = 'Tariff'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
