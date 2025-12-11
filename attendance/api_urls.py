from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import StudentViewSet, ClassroomViewSet, AttendanceRecordViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='api-student')
router.register(r'classrooms', ClassroomViewSet, basename='api-classroom')
router.register(r'attendance', AttendanceRecordViewSet, basename='api-attendance')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
