from django import forms
from .models import Student, Classroom, AttendanceRecord


class StudentForm(forms.ModelForm):
    """Form for creating/updating Student."""
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'course_or_year_level', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2024-0001'}),
            'course_or_year_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1st Year BSCS'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ClassroomForm(forms.ModelForm):
    """Form for creating/updating Classroom."""
    
    class Meta:
        model = Classroom
        fields = ['name', 'code', 'schedule', 'teacher_name', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject/Class Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., CS101'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., MWF 9:00-10:00 AM'}),
            'teacher_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher Name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AttendanceRecordForm(forms.ModelForm):
    """Form for creating/updating AttendanceRecord."""
    
    class Meta:
        model = AttendanceRecord
        fields = ['student', 'classroom', 'date', 'status', 'remarks']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'classroom': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional remarks'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter only active students and classrooms
        self.fields['student'].queryset = Student.objects.filter(is_active=True)
        self.fields['classroom'].queryset = Classroom.objects.filter(is_active=True)


class AttendanceFilterForm(forms.Form):
    """Form for filtering attendance records."""
    student = forms.ModelChoiceField(
        queryset=Student.objects.filter(is_active=True),
        required=False,
        empty_label="All Students",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.filter(is_active=True),
        required=False,
        empty_label="All Classes",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    status = forms.ChoiceField(
        choices=[('', 'All Statuses')] + AttendanceRecord.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
