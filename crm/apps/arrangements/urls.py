from django.urls import path, include
from rest_framework import routers

from .views import *

group_router = routers.SimpleRouter()
group_router.register(r'groups', GroupView)

urlpatterns = [
    path('auditoriums', AuditoriumView.as_view(), name="auditorium-list"),
    path('', include(group_router.urls)),
] 

