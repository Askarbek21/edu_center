from rest_framework import viewsets
from crm.utils import is_owner

from .serializers import *
from .filters import StudentFilter, TeacherFilter


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filterset_class = StudentFilter
    view_permissions = {
        'options': {'admin': True},
        'create': {'admin': True},
        'list': {'admin': True},
        'retrieve': {'user': is_owner, 'admin':True},
        'update,partial_update': {'admin':True},
        'destroy': {'admin':True},
    }


class TeacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filterset_class = TeacherFilter
    view_permissions = {
        'options': {'admin':True},
        'create': {'admin': True},
        'list': {'admin': True},
        'retrieve': {'user': is_owner, 'admin':True},
        'update,partial_update': {'admin':True},
        'destroy': {'admin':True},
    }


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    view_permissions = {
        'options': {'admin':True},
        'create': {'admin': True},
        'list': {'admin': True},
        'retrieve': {'admin':True},
        'update,partial_update': {'admin':True},
        'destroy': {'admin':True},
    }


