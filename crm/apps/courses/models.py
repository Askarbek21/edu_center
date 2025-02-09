import datetime
from django.db import models
from django.utils.text import slugify

from apps.branches.models import Branch
from apps.users.models import CustomUser

class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE ,null=True, related_name='student_profile')
    first_name = models.CharField(max_length=64, verbose_name='Имя студента')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия студента')
    phone_number = models.CharField(max_length=13, verbose_name='Телефон номер')
    has_paid = models.BooleanField(default=False, verbose_name='Оплатил')
    parents_phone_number = models.CharField(max_length=13, verbose_name='Телефон номер родителей', blank=True)
    joined_date = models.DateField(default=datetime.date.today, verbose_name='Дата присоединение')
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, verbose_name='Статус')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, 
        related_name='students', 
        verbose_name="Филиал",
        null=True
    )

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='teacher_profile')
    name = models.CharField(max_length=128, verbose_name='ФИО')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='teachers_img/', verbose_name='Фото учителя', null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс', null=True)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='branch_teachers', verbose_name="Филиал",
        null=True
    )

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя курса', unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    duration = models.CharField(max_length=64, verbose_name='Длительность курса')
    img = models.ImageField(upload_to='courses_img/', verbose_name='Фото')
    slug = models.SlugField(max_length=128, unique=True)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='branch_courses', verbose_name="Филиал",
        null=True
    )

    class Meta:
        db_table = 'course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    

class Status(models.Model):
    name = models.CharField(max_length=128, verbose_name='Статус')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        