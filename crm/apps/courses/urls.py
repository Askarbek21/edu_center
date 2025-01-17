from django.urls import path, include
from rest_framework import routers

from .views import *

teacher_router = routers.SimpleRouter()
student_router = routers.SimpleRouter()
course_router = routers.SimpleRouter()

teacher_router.register(r'teachers', TeacherView)
student_router.register(r'students', StudentView)
course_router.register(r'courses', CourseView)

urlpatterns = [
    path('', include(teacher_router.urls)),
    path('', include(student_router.urls)),
    path('', include(course_router.urls)),
]
