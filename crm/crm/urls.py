from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arrangements/', include('apps.arrangements.urls')),
    path('main/', include('apps.courses.urls')),
    path('auth/', include('rest_framework.urls'))
]
