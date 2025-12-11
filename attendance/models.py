from django.db import models
from django.core.validators import MinLengthValidator


class Student(models.Model):
    """Model representing a student."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(
        max_length=20, 
        unique=True,
        validators=[MinLengthValidator(3)],
        help_text="Unique student ID"
    )
    course_or_year_level = models.CharField(
        max_length=100,
        help_text="e.g., '1st Year BSCS', '2nd Year BSIT'"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.student_id} - {self.last_name}, {self.first_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Classroom(models.Model):
    """Model representing a classroom/subject."""
    name = models.CharField(max_length=200, help_text="Subject/Class name")
    code = models.CharField(
        max_length=20, 
        unique=True,
        help_text="Unique class code (e.g., CS101)"
    )
    schedule = models.CharField(
        max_length=200,
        help_text="e.g., 'MWF 9:00-10:00 AM'"
    )
    teacher_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return f"{self.code} - {self.name}"


class AttendanceRecord(models.Model):
    """Model representing an attendance record."""
    
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
        ('EXCUSED', 'Excused'),
    ]

    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PRESENT'
    )
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'classroom', 'student']
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'
        unique_together = ['student', 'classroom', 'date']

    def __str__(self):
        return f"{self.student.student_id} - {self.classroom.code} - {self.date} - {self.status}"
