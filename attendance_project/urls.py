"""
URL configuration for attendance_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
    path('api/', include('attendance.api_urls')),
]
