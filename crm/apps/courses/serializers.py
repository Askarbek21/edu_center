from rest_framework import serializers

from .models import *
from apps.arrangements.models import Group


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    group = serializers.SlugRelatedField(slug_field="name", queryset=Group.objects.all(), required=False)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone_number', 'parents_phone_number', 'group', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', [])

        new_student = Student(**validated_data)

        if password:
            new_user = CustomUser(
            phone_number=validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            role="Student",
            )
            new_user.set_password(password)
            new_user.save()
            new_student.user = new_user

        new_student.save()
        return new_student


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Teacher
        fields = ['name', 'phone_number', 'img', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', [])

        new_teacher = Teacher(**validated_data)

        if password:
            new_user = CustomUser(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['name'],
            role="Teacher",
            )
            new_user.set_password(password)
            new_user.save()
            new_teacher.user = new_user

        new_teacher.save()
        return new_teacher


class CourseSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(slug_field="name", queryset=Branch.objects.all())
    class Meta:
        model = Course
        fields = ['name', 'price', 'duration', 'img', 'branch']
