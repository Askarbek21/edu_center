import datetime
from django.db import models
from django.utils.text import slugify

from apps.branches.models import Branch
from apps.courses.models import Teacher, Student, Course


class Group(models.Model):
    DAYS_CHOICES = [
        ('Четные', 'Четные'),
        ('Нечетные', 'Нечетные')
    ]
    STATUS_CHOICES = {
        "Неактивный": "Неактивный",
        "Активный": "Активный",
        "Завершенный": "Завершенный",
    }
    name = models.CharField(max_length=64, verbose_name='Название группы')
    start_date = models.DateField(verbose_name='Дата начала группы', default=datetime.date.today)
    end_date = models.DateField(verbose_name='Дата завершения группы')
    start_time = models.TimeField(verbose_name='Начало занятия')
    end_time = models.TimeField(verbose_name='Конец занятия')
    lesson_days = models.CharField(max_length=8,choices=DAYS_CHOICES, default='Четные', verbose_name='День занятия')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='Неактивный', verbose_name='Статус группы')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    auditorium = models.ForeignKey('Auditorium', on_delete=models.PROTECT, verbose_name='Аудитория')
    students = models.ManyToManyField(Student, related_name='student_groups', verbose_name='Студенты')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='branch_groups', verbose_name="Филиал",
        null=True
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['status']


class Auditorium(models.Model):
    name = models.CharField(max_length=64, verbose_name='Аудитория')
    floor_number = models.PositiveSmallIntegerField(default=1, verbose_name='Этаж')
    capacity = models.PositiveSmallIntegerField(verbose_name='Вместимость')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='audiences', verbose_name="Филиал",
        null=True
    )

    class Meta:
        db_table = 'auditorium'
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()


class Attendance(models.Model):
    date = models.DateField(verbose_name='Дата пропуска')
    is_present = models.BooleanField(verbose_name='Присутствует')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='attendances', verbose_name="Филиал",
        null=True
    )

    class Meta:
        db_table = 'attendance'
        verbose_name = 'Посещение студента'
        verbose_name_plural = 'Посещения студентов'