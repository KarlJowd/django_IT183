# STUDENT ATTENDANCE TRACKER - COMPLETE SETUP GUIDE

## 🚀 Quick Start Instructions

### 1. Install Dependencies
```bash
cd attendance_system
pip install -r requirements.txt
```

### 2. Create Database and Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (for Django Admin)
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: admin123
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

### 5. Access the Application
- **Main App**: http://localhost:8000/
- **Django Admin**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/

---

## 📁 Complete Project Structure

```
attendance_system/
├── manage.py
├── requirements.txt
├── db.sqlite3 (created after migrations)
│
├── attendance_project/
│   ├── __init__.py
│   ├── settings.py      # Main settings with REST framework config
│   ├── urls.py          # Project URLs
│   ├── wsgi.py
│   └── asgi.py
│
└── attendance/
    ├── __init__.py
    ├── admin.py         # Admin customization
    ├── apps.py
    ├── models.py        # Student, Classroom, AttendanceRecord
    ├── serializers.py   # DRF serializers
    ├── viewsets.py      # DRF viewsets
    ├── views.py         # Django views for web UI
    ├── forms.py         # Django forms
    ├── urls.py          # App URLs (web interface)
    ├── api_urls.py      # API URLs (REST framework)
    ├── migrations/      # Database migrations
    │
    ├── templates/
    │   └── attendance/
    │       ├── base.html
    │       ├── home.html
    │       ├── student_list.html
    │       ├── student_form.html
    │       ├── student_detail.html
    │       ├── student_confirm_delete.html
    │       ├── classroom_list.html
    │       ├── classroom_form.html
    │       ├── classroom_confirm_delete.html
    │       ├── attendance_list.html
    │       ├── attendance_form.html
    │       ├── attendance_confirm_delete.html
    │       └── report.html
    │
    └── static/
        └── attendance/
            └── (custom CSS/JS if needed)
```

---

## 🎯 PRESENTATION SCRIPT (20 POINTS)

### **Introduction (30 seconds)**

"Good day! Today I'm presenting the **Student Attendance Tracker**, a comprehensive web application built with Django and Bootstrap 5.

This system helps **teachers and school administrators** efficiently manage and monitor student attendance across multiple classrooms. It provides:
- Easy attendance recording
- Real-time attendance tracking
- Comprehensive reporting and analytics
- RESTful API for integration with other systems"

---

### **Feature Demonstration (5-7 minutes)**

#### **1. Dashboard Overview (30 seconds)**
"Let's start with the dashboard which shows:
- Total active students, classrooms, and attendance records
- Quick action buttons for common tasks
- Recent attendance activity"

**Navigation**: Open http://localhost:8000/

---

#### **2. Student Management - CRUD Demo (1.5 minutes)**

"Now let's demonstrate full CRUD operations for students..."

**CREATE:**
- Click "Students" → "Add New Student"
- Fill in form:
  - First Name: Juan
  - Last Name: Dela Cruz
  - Student ID: 2024-0001
  - Course/Year: 1st Year BSCS
  - Status: Active ✓
- Click "Save Student"
- **Show success message**

**READ:**
- View student list showing all students in a Bootstrap table
- Click on student name to view detailed profile
- **Point out**: Recent attendance records displayed on detail page

**UPDATE:**
- Click "Edit" button on a student
- Modify course to "2nd Year BSCS"
- Save changes

**DELETE:**
- Click "Delete" button
- Show confirmation dialog with warning
- (Cancel to preserve data for demo)

---

#### **3. Classroom Management - CRUD Demo (1 minute)**

"Similar CRUD operations for classrooms..."

**CREATE a classroom:**
- Navigate to "Classes" → "Add New Classroom"
- Fill in:
  - Name: Introduction to Programming
  - Code: CS101
  - Schedule: MWF 9:00-10:00 AM
  - Teacher: Prof. Maria Santos
  - Active: ✓
- Save

**Show list** of all classrooms with edit/delete actions

---

#### **4. Attendance Recording - CRUD Demo (1.5 minutes)**

"The core feature - attendance tracking..."

**CREATE attendance record:**
- Navigate to "Attendance" → "Record Attendance"
- Select:
  - Student: Juan Dela Cruz
  - Classroom: CS101
  - Date: (Today's date - pre-filled)
  - Status: Present
  - Remarks: (Optional)
- Save

**FILTER functionality:**
- Show filter form at top of attendance list
- Filter by:
  - Specific student
  - Specific classroom
  - Date range (from/to)
  - Status (Present/Absent/Late/Excused)
- Apply filters

**UPDATE/DELETE:**
- Show edit functionality
- Show delete confirmation

---

#### **5. Reports - EXTRA FEATURE (+20 POINTS) - (2 minutes)**

"This is our **additional feature** beyond basic CRUD - the Attendance Summary Report..."

**Navigate to "Reports":**

**Explain what's shown:**
- "For each active student, the system calculates:
  - Total attendance records
  - Breakdown: Present, Absent, Late, Excused
  - **Attendance Percentage** (Present + Late / Total)
  - Color-coded indicators:
    - Green (≥75%) = Good attendance
    - Yellow (50-74%) = Needs improvement  
    - Red (<50%) = At risk"

**Demonstrate filtering:**
- Filter by specific classroom
- Filter by date range (from/to)
- Click "Apply" to see updated statistics

**Highlight the value:**
"This helps administrators quickly identify at-risk students and intervene early."

---

#### **6. Django Admin (1 minute)**

"Now let's look at Django's admin interface..."

**Open**: http://localhost:8000/admin/
- Login with superuser credentials

**Show customization:**
- Click "Students" - show list_display, filters, search
- Click "Attendance Records" - show date hierarchy, status filters
- **Explain**: "Django admin provides a quick way for staff to manage data without using the main interface"

---

### **API Testing (3-5 minutes - 30 POINTS)**

"Now let's test the RESTful API..."

#### **Setup:**
Use **Postman** or browser's address bar for GET requests, Postman for POST/PUT/DELETE.

**API Endpoints:**
```
/api/students/
/api/classrooms/
/api/attendance/
```

---

#### **1. GET Request - List All Students**
```
GET http://localhost:8000/api/students/
```

**Show response** (JSON):
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "first_name": "Juan",
      "last_name": "Dela Cruz",
      "full_name": "Juan Dela Cruz",
      "student_id": "2024-0001",
      "course_or_year_level": "1st Year BSCS",
      "is_active": true,
      "created_at": "2024-12-12T10:30:00Z",
      "updated_at": "2024-12-12T10:30:00Z"
    }
  ]
}
```

---

#### **2. POST Request - Create New Student**
```
POST http://localhost:8000/api/students/
Content-Type: application/json

{
  "first_name": "Maria",
  "last_name": "Santos",
  "student_id": "2024-0002",
  "course_or_year_level": "1st Year BSIT",
  "is_active": true
}
```

**Show**: 201 Created response with new student data

---

#### **3. GET Request - Retrieve Single Student**
```
GET http://localhost:8000/api/students/1/
```

**Show**: Detailed student information

---

#### **4. PUT/PATCH Request - Update Student**
```
PATCH http://localhost:8000/api/students/1/
Content-Type: application/json

{
  "course_or_year_level": "2nd Year BSCS"
}
```

**Show**: 200 OK response with updated data

---

#### **5. DELETE Request - Delete Student**
```
DELETE http://localhost:8000/api/students/2/
```

**Show**: 204 No Content response

---

#### **Repeat for Classrooms:**

**POST - Create Classroom:**
```
POST http://localhost:8000/api/classrooms/
Content-Type: application/json

{
  "name": "Data Structures",
  "code": "CS102",
  "schedule": "TTh 1:00-2:30 PM",
  "teacher_name": "Prof. Jose Rizal",
  "is_active": true
}
```

---

#### **And Attendance Records:**

**POST - Create Attendance Record:**
```
POST http://localhost:8000/api/attendance/
Content-Type: application/json

{
  "student": 1,
  "classroom": 1,
  "date": "2024-12-12",
  "status": "PRESENT",
  "remarks": "On time"
}
```

**Show filtering:**
```
GET /api/attendance/?student=1
GET /api/attendance/?classroom=1
GET /api/attendance/?status=PRESENT
GET /api/attendance/?date=2024-12-12
```

---

### **Django Understanding Explanation (2-3 minutes - Part of grading)**

"Let me briefly explain how Django components work together in this project..."

#### **1. Models → Database**
"Models (Student, Classroom, AttendanceRecord) define our database schema.
- Each model class becomes a database table
- Django ORM handles SQL automatically
- Relationships: ForeignKey creates many-to-one relationships"

#### **2. Views → Business Logic**
"Views handle the logic:
- Function-based views process requests
- They fetch data from models
- Apply business logic (filtering, calculations)
- Return responses (render templates or JSON)"

#### **3. Templates → UI**
"Templates display data:
- base.html provides consistent layout (navbar, footer)
- Child templates extend base and add specific content
- Django template language: {% %} for logic, {{ }} for variables
- Bootstrap 5 classes style everything"

#### **4. URLs → Routing**
"URL patterns map URLs to views:
- Project urls.py routes to app URLs
- App urls.py maps specific paths to views
- Name attribute allows reverse URL lookup"

#### **5. Django Admin**
"Admin is auto-generated from models:
- Register models in admin.py
- Customize with list_display, list_filter, search_fields
- Provides instant CRUD interface"

#### **6. Django REST Framework → API**
"DRF provides the API:
- Serializers convert models to/from JSON
- ViewSets provide CRUD operations
- Router auto-generates URL patterns
- FilterBackends enable querying"

---

### **Conclusion (30 seconds)**

"In summary, this Student Attendance Tracker demonstrates:
✅ Full CRUD operations (50 points Functionality)
✅ Additional reporting feature (20 points Functionality)
✅ Clean, responsive Bootstrap 5 UI (30 points UI)
✅ Complete RESTful API with filtering (30 points API)
✅ Comprehensive Django understanding

The system is production-ready and can be deployed to Google IDX or any Django-compatible hosting platform.

Thank you! Any questions?"

---

## 📊 API Testing Examples Summary

### Example Request Bodies:

#### Create Student:
```json
{
  "first_name": "Pedro",
  "last_name": "Penduko",
  "student_id": "2024-0003",
  "course_or_year_level": "3rd Year BSCS",
  "is_active": true
}
```

#### Create Classroom:
```json
{
  "name": "Object-Oriented Programming",
  "code": "CS103",
  "schedule": "MWF 2:00-3:30 PM",
  "teacher_name": "Prof. Andres Bonifacio",
  "is_active": true
}
```

#### Create Attendance Record:
```json
{
  "student": 1,
  "classroom": 1,
  "date": "2024-12-12",
  "status": "PRESENT",
  "remarks": ""
}
```

**Status choices**: PRESENT, ABSENT, LATE, EXCUSED

---

## 🔧 Troubleshooting

### If you get "Table doesn't exist" errors:
```bash
python manage.py makemigrations attendance
python manage.py migrate
```

### To reset database:
```bash
# Delete db.sqlite3 file
python manage.py migrate
python manage.py createsuperuser
```

### To populate test data (optional):
Create a management command or use Django admin to add sample data.

---

## ✅ Grading Checklist

### Functionality (70 points):
- [x] Student CRUD (Create, Read, Update, Delete)
- [x] Classroom CRUD
- [x] Attendance Record CRUD
- [x] Filtering on attendance list
- [x] **EXTRA FEATURE (+20)**: Attendance Summary Report with statistics

### UI (30 points):
- [x] Bootstrap 5 implementation
- [x] Consistent base template with navbar
- [x] Responsive design
- [x] Clean, professional appearance
- [x] Proper use of cards, tables, forms
- [x] Status badges and icons

### API (30 points):
- [x] REST API for all models
- [x] All CRUD operations via API
- [x] Proper serializers
- [x] Filtering capabilities
- [x] Proper HTTP status codes

### Presentation (20 points):
- [x] Clear explanation of features
- [x] Live demonstration of all CRUD
- [x] API testing with Postman
- [x] Django concept explanations
- [x] Extra feature highlighted

**TOTAL: 150 points possible**

---

## 🎓 Key Features to Emphasize

1. **Complete CRUD** for all three models
2. **Relationships**: Student ← AttendanceRecord → Classroom
3. **Validation**: Unique constraints, required fields
4. **Business Logic**: Attendance percentage calculation
5. **Filtering**: Multiple filter options
6. **Admin Customization**: List display, filters, search
7. **API**: Full REST implementation
8. **UI/UX**: Modern Bootstrap 5 design
9. **Extra Feature**: Comprehensive reporting system

Good luck with your presentation! 🚀
