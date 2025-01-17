from rest_framework import serializers

from apps.courses.models import Course
from .models import *


class GroupSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field="name", queryset=Course.objects.all())
    teacher = serializers.SlugRelatedField(slug_field="name", queryset=Teacher.objects.all())
    auditorium = serializers.SlugRelatedField(slug_field="name", queryset=Auditorium.objects.all())
    class Meta:
        model = Group
        fields = [
            'name','course','start_date', 'end_date', 'start_time',
            'end_time', 'lesson_days', 'teacher', 'auditorium',
            'status', 'branch'
            ]


class AuditoriumSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(slug_field="name", queryset=Branch.objects.all())
    class Meta:
        model = Auditorium
        fields = ['name', 'floor_number','capacity', 'branch']
