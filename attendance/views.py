from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone
from datetime import datetime
from .models import Student, Classroom, AttendanceRecord
from .forms import StudentForm, ClassroomForm, AttendanceRecordForm, AttendanceFilterForm


# ================== HOME / DASHBOARD ==================
def home(request):
    """Dashboard/Home page."""
    context = {
        'total_students': Student.objects.filter(is_active=True).count(),
        'total_classrooms': Classroom.objects.filter(is_active=True).count(),
        'total_records': AttendanceRecord.objects.count(),
        'recent_records': AttendanceRecord.objects.select_related('student', 'classroom').order_by('-date', '-created_at')[:10],
    }
    return render(request, 'attendance/home.html', context)


# ================== STUDENT CRUD ==================
def student_list(request):
    """List all students."""
    students = Student.objects.all().order_by('-is_active', 'last_name', 'first_name')
    return render(request, 'attendance/student_list.html', {'students': students})


def student_create(request):
    """Create a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.get_full_name()} created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'attendance/student_form.html', {'form': form, 'action': 'Create'})


def student_update(request, pk):
    """Update an existing student."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.get_full_name()} updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'attendance/student_form.html', {'form': form, 'action': 'Update', 'student': student})


def student_delete(request, pk):
    """Delete a student."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_name = student.get_full_name()
        student.delete()
        messages.success(request, f'Student {student_name} deleted successfully!')
        return redirect('student_list')
    return render(request, 'attendance/student_confirm_delete.html', {'student': student})


def student_detail(request, pk):
    """View student details with recent attendance."""
    student = get_object_or_404(Student, pk=pk)
    recent_attendance = AttendanceRecord.objects.filter(student=student).select_related('classroom').order_by('-date')[:10]
    
    # Calculate statistics
    total_records = AttendanceRecord.objects.filter(student=student).count()
    present_count = AttendanceRecord.objects.filter(student=student, status='PRESENT').count()
    absent_count = AttendanceRecord.objects.filter(student=student, status='ABSENT').count()
    late_count = AttendanceRecord.objects.filter(student=student, status='LATE').count()
    excused_count = AttendanceRecord.objects.filter(student=student, status='EXCUSED').count()
    
    attendance_percentage = (present_count / total_records * 100) if total_records > 0 else 0
    
    context = {
        'student': student,
        'recent_attendance': recent_attendance,
        'total_records': total_records,
        'present_count': present_count,
        'absent_count': absent_count,
        'late_count': late_count,
        'excused_count': excused_count,
        'attendance_percentage': round(attendance_percentage, 2),
    }
    return render(request, 'attendance/student_detail.html', context)


# ================== CLASSROOM CRUD ==================
def classroom_list(request):
    """List all classrooms."""
    classrooms = Classroom.objects.all().order_by('-is_active', 'code')
    return render(request, 'attendance/classroom_list.html', {'classrooms': classrooms})


def classroom_create(request):
    """Create a new classroom."""
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save()
            messages.success(request, f'Classroom {classroom.code} created successfully!')
            return redirect('classroom_list')
    else:
        form = ClassroomForm()
    return render(request, 'attendance/classroom_form.html', {'form': form, 'action': 'Create'})


def classroom_update(request, pk):
    """Update an existing classroom."""
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            classroom = form.save()
            messages.success(request, f'Classroom {classroom.code} updated successfully!')
            return redirect('classroom_list')
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'attendance/classroom_form.html', {'form': form, 'action': 'Update', 'classroom': classroom})


def classroom_delete(request, pk):
    """Delete a classroom."""
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        classroom_code = classroom.code
        classroom.delete()
        messages.success(request, f'Classroom {classroom_code} deleted successfully!')
        return redirect('classroom_list')
    return render(request, 'attendance/classroom_confirm_delete.html', {'classroom': classroom})


# ================== ATTENDANCE CRUD ==================
def attendance_list(request):
    """List all attendance records with filtering."""
    records = AttendanceRecord.objects.select_related('student', 'classroom').all()
    filter_form = AttendanceFilterForm(request.GET)
    
    # Apply filters
    if filter_form.is_valid():
        student = filter_form.cleaned_data.get('student')
        classroom = filter_form.cleaned_data.get('classroom')
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')
        status = filter_form.cleaned_data.get('status')
        
        if student:
            records = records.filter(student=student)
        if classroom:
            records = records.filter(classroom=classroom)
        if date_from:
            records = records.filter(date__gte=date_from)
        if date_to:
            records = records.filter(date__lte=date_to)
        if status:
            records = records.filter(status=status)
    
    records = records.order_by('-date', 'classroom', 'student')
    
    context = {
        'records': records,
        'filter_form': filter_form,
    }
    return render(request, 'attendance/attendance_list.html', context)


def attendance_create(request):
    """Create a new attendance record."""
    if request.method == 'POST':
        form = AttendanceRecordForm(request.POST)
        if form.is_valid():
            try:
                record = form.save()
                messages.success(request, f'Attendance record created successfully!')
                return redirect('attendance_list')
            except Exception as e:
                messages.error(request, f'Error creating record: {str(e)}')
    else:
        # Pre-fill with today's date
        form = AttendanceRecordForm(initial={'date': timezone.now().date()})
    return render(request, 'attendance/attendance_form.html', {'form': form, 'action': 'Create'})


def attendance_update(request, pk):
    """Update an existing attendance record."""
    record = get_object_or_404(AttendanceRecord, pk=pk)
    if request.method == 'POST':
        form = AttendanceRecordForm(request.POST, instance=record)
        if form.is_valid():
            try:
                record = form.save()
                messages.success(request, f'Attendance record updated successfully!')
                return redirect('attendance_list')
            except Exception as e:
                messages.error(request, f'Error updating record: {str(e)}')
    else:
        form = AttendanceRecordForm(instance=record)
    return render(request, 'attendance/attendance_form.html', {'form': form, 'action': 'Update', 'record': record})


def attendance_delete(request, pk):
    """Delete an attendance record."""
    record = get_object_or_404(AttendanceRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, f'Attendance record deleted successfully!')
        return redirect('attendance_list')
    return render(request, 'attendance/attendance_confirm_delete.html', {'record': record})

