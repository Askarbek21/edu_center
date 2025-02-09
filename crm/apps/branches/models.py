from django.db import models

from apps.organisation.models import Organisation

class Branch(models.Model):
    name = models.CharField("Название филиала", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    phone_number = models.CharField("Телефон", max_length=13)
    logo = models.ImageField(upload_to="logo", verbose_name='Лого филиала')
    short_logo = models.ImageField(upload_to="logo", verbose_name='Короткий логотип филиала')
    admin = models.ForeignKey(
        'users.CustomUser', on_delete=models.CASCADE,
        related_name='admin_branches',
        verbose_name="Админ филиала"
    )
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='main_branches', )

    class Meta:
        db_table = 'branch'
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
        ordering = ['name']

    def __str__(self):
        return self.name
