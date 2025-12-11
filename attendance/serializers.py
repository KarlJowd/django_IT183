from rest_framework import serializers
from .models import Student, Classroom, AttendanceRecord


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model."""
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'full_name',
            'student_id', 
            'course_or_year_level', 
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ClassroomSerializer(serializers.ModelSerializer):
    """Serializer for Classroom model."""
    
    class Meta:
        model = Classroom
        fields = [
            'id',
            'name',
            'code',
            'schedule',
            'teacher_name',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AttendanceRecordSerializer(serializers.ModelSerializer):
    """Serializer for AttendanceRecord model."""
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    student_id_display = serializers.CharField(source='student.student_id', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)
    classroom_code = serializers.CharField(source='classroom.code', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = AttendanceRecord
        fields = [
            'id',
            'student',
            'student_name',
            'student_id_display',
            'classroom',
            'classroom_name',
            'classroom_code',
            'date',
            'status',
            'status_display',
            'remarks',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        """Check for duplicate attendance records."""
        student = data.get('student')
        classroom = data.get('classroom')
        date = data.get('date')
        
        # If updating, exclude the current instance
        queryset = AttendanceRecord.objects.filter(
            student=student,
            classroom=classroom,
            date=date
        )
        
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError(
                "An attendance record for this student in this classroom on this date already exists."
            )
        
        return data
