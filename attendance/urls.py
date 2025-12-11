from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Students
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    
    # Classrooms
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('classrooms/create/', views.classroom_create, name='classroom_create'),
    path('classrooms/<int:pk>/update/', views.classroom_update, name='classroom_update'),
    path('classrooms/<int:pk>/delete/', views.classroom_delete, name='classroom_delete'),
    
    # Attendance
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:pk>/update/', views.attendance_update, name='attendance_update'),
    path('attendance/<int:pk>/delete/', views.attendance_delete, name='attendance_delete'),
    
    # Reports (Extra Feature)
    path('reports/', views.attendance_report, name='attendance_report'),
]
