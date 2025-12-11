from django.contrib import admin
from .models import Student, Classroom, AttendanceRecord


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin configuration for Student model."""
    list_display = ['student_id', 'last_name', 'first_name', 'course_or_year_level', 'is_active', 'created_at']
    list_filter = ['is_active', 'course_or_year_level', 'created_at']
    search_fields = ['first_name', 'last_name', 'student_id', 'course_or_year_level']
    ordering = ['last_name', 'first_name']
    list_per_page = 25
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'student_id')
        }),
        ('Academic Information', {
            'fields': ('course_or_year_level', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    """Admin configuration for Classroom model."""
    list_display = ['code', 'name', 'teacher_name', 'schedule', 'is_active', 'created_at']
    list_filter = ['is_active', 'teacher_name', 'created_at']
    search_fields = ['name', 'code', 'teacher_name']
    ordering = ['code']
    list_per_page = 25
    
    fieldsets = (
        ('Class Information', {
            'fields': ('name', 'code', 'teacher_name')
        }),
        ('Schedule', {
            'fields': ('schedule', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    """Admin configuration for AttendanceRecord model."""
    list_display = ['date', 'student', 'classroom', 'status', 'created_at']
    list_filter = ['status', 'date', 'classroom', 'created_at']
    search_fields = [
        'student__first_name', 
        'student__last_name', 
        'student__student_id',
        'classroom__name',
        'classroom__code'
    ]
    ordering = ['-date', 'classroom', 'student']
    list_per_page = 50
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Attendance Information', {
            'fields': ('student', 'classroom', 'date', 'status')
        }),
        ('Additional Details', {
            'fields': ('remarks',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    # Inline filtering
    autocomplete_fields = []  # Add if you want autocomplete for foreign keys
    
    def get_queryset(self, request):
        """Optimize queryset with select_related."""
        queryset = super().get_queryset(request)
        return queryset.select_related('student', 'classroom')
