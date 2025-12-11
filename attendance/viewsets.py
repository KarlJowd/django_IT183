from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, Classroom, AttendanceRecord
from .serializers import StudentSerializer, ClassroomSerializer, AttendanceRecordSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Students.
    Supports: GET list, GET detail, POST, PUT, PATCH, DELETE
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'course_or_year_level']
    search_fields = ['first_name', 'last_name', 'student_id']
    ordering_fields = ['last_name', 'student_id', 'created_at']
    ordering = ['last_name', 'first_name']


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Classrooms.
    Supports: GET list, GET detail, POST, PUT, PATCH, DELETE
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'teacher_name']
    search_fields = ['name', 'code', 'teacher_name']
    ordering_fields = ['code', 'name', 'created_at']
    ordering = ['code']


class AttendanceRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Attendance Records.
    Supports: GET list, GET detail, POST, PUT, PATCH, DELETE
    
    Filter examples:
    - /api/attendance/?student=1
    - /api/attendance/?classroom=2
    - /api/attendance/?status=PRESENT
    - /api/attendance/?date=2024-01-15
    """
    queryset = AttendanceRecord.objects.select_related('student', 'classroom').all()
    serializer_class = AttendanceRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'classroom', 'status', 'date']
    search_fields = ['student__student_id', 'student__first_name', 'student__last_name', 'classroom__code']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date', 'classroom', 'student']
