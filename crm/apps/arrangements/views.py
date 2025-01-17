from django.shortcuts import render
from rest_framework import generics, viewsets

from .serializers import GroupSerializer, AuditoriumSerializer
from .models import Group, Auditorium
from .filters import GroupFilter

class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filterset_class = GroupFilter


class AuditoriumView(generics.ListCreateAPIView):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()


class AttendanceView(generics.ListCreateAPIView):
    pass
