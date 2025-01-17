from django.shortcuts import render
from rest_framework import generics, viewsets

from .serializers import GroupSerializer, AuditoriumSerializer
from .models import Group, Auditorium
from .filters import GroupFilter


class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filterset_class = GroupFilter
    view_permissions = {
        'options': {'admin': True},
        'create': {'admin': True},
        'list': {'admin': True},
        'retrieve': {'admin':True},
        'update,partial_update': {'admin':True},
        'destroy': {'admin':True},
    }


class AuditoriumView(generics.ListCreateAPIView):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()
    view_permissions = {
        'options': {'admin':True},
        'post': {'admin': True},
        'get': {'admin': True},
    }

class AttendanceView(generics.ListCreateAPIView):
    pass
