from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Student, Teacher


class StudentFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_by_name_phone')
    course = filters.CharFilter(lookup_expr='iexact')
    status = filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Student
        fields = ['course', 'status']

    def filter_by_name_phone(self,queryset,last_name,value):
        return queryset.filter(Q(last_name__icontains=value) | Q(phone_number__iexact=value))


class TeacherFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_by_name_phone')
    class Meta:
        model = Teacher
        fields = []

    def filter_by_name_phone(self,queryset,name,value):
        return queryset.filter(Q(name__icontains=value) | Q(phone_number__iexact=value))
    