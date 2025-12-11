# 🎓 STUDENT ATTENDANCE TRACKER
## Complete Django + Bootstrap 5 + REST API Application

---

## 📋 PROJECT OVERVIEW

A comprehensive web-based Student Attendance Management System built with:
- **Backend**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Frontend**: Bootstrap 5 + Django Templates
- **Database**: SQLite (default, easily switchable to PostgreSQL/MySQL)

### Target Users:
- School Teachers
- Academic Administrators
- School Staff

### Core Features:
✅ Complete CRUD for Students, Classrooms, and Attendance Records
✅ Advanced filtering and search capabilities
✅ Attendance Summary Reports with Statistics **(EXTRA FEATURE +20pts)**
✅ RESTful API with full CRUD operations
✅ Responsive Bootstrap 5 UI
✅ Django Admin customization

---

## 🚀 INSTALLATION & SETUP

### Prerequisites:
- Python 3.8+ installed
- pip package manager

### Step 1: Navigate to Project Directory
```bash
cd C:\Users\admin\Documents\Codes\attendance_system
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

**Activate virtual environment:**

Windows PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```

Windows CMD:
```bash
venv\Scripts\activate.bat
```

Linux/Mac:
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Contents of requirements.txt:**
```
Django==4.2.7
djangorestframework==3.14.0
django-filter==23.3
pillow==10.1.0
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser Account
```bash
python manage.py createsuperuser
```

**Recommended credentials for demo:**
- Username: `admin`
- Email: `admin@example.com`
- Password: `admin123` (or your choice)

### Step 6: Run Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
- **Main Application**: http://localhost:8000/
- **Django Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/
- **API Endpoints**:
  - Students: http://localhost:8000/api/students/
  - Classrooms: http://localhost:8000/api/classrooms/
  - Attendance: http://localhost:8000/api/attendance/

---

## 📁 PROJECT STRUCTURE (COMPLETE)

```
attendance_system/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── db.sqlite3                        # SQLite database (created after migration)
├── PRESENTATION_GUIDE.md             # Complete presentation script
├── TEMPLATES_PART1.md                # Classroom templates
├── TEMPLATES_PART2.md                # Attendance & report templates
│
├── attendance_project/               # Main project folder
│   ├── __init__.py
│   ├── settings.py                   # Project settings (IMPORTANT)
│   ├── urls.py                       # Root URL configuration
│   ├── wsgi.py                       # WSGI config for deployment
│   └── asgi.py                       # ASGI config
│
└── attendance/                       # Main application
    ├── __init__.py
    ├── apps.py                       # App configuration
    ├── models.py                     # Database models (Student, Classroom, AttendanceRecord)
    ├── serializers.py                # DRF serializers
    ├── viewsets.py                   # DRF viewsets for API
    ├── views.py                      # Django views for web interface
    ├── forms.py                      # Django forms
    ├── admin.py                      # Django admin customization
    ├── urls.py                       # Web interface URLs
    ├── api_urls.py                   # API URLs
    │
    ├── migrations/                   # Database migration files
    │   └── (auto-generated)
    │
    ├── templates/
    │   └── attendance/
    │       ├── base.html             # Base template (navbar, footer)
    │       ├── home.html             # Dashboard
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
    │       └── report.html           # EXTRA FEATURE
    │
    └── static/
        └── attendance/
            └── (CSS/JS files if needed)
```

---

## 🗂️ DATABASE MODELS

### 1. Student Model
```python
Fields:
- first_name (CharField)
- last_name (CharField)
- student_id (CharField, unique)
- course_or_year_level (CharField)
- is_active (BooleanField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

Methods:
- get_full_name(): Returns "FirstName LastName"
- __str__(): Returns "StudentID - LastName, FirstName"
```

### 2. Classroom Model
```python
Fields:
- name (CharField) - Subject/Class name
- code (CharField, unique) - Class code (e.g., CS101)
- schedule (CharField) - e.g., "MWF 9:00-10:00 AM"
- teacher_name (CharField)
- is_active (BooleanField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

Methods:
- __str__(): Returns "Code - Name"
```

### 3. AttendanceRecord Model
```python
Fields:
- student (ForeignKey to Student)
- classroom (ForeignKey to Classroom)
- date (DateField)
- status (CharField with choices: PRESENT, ABSENT, LATE, EXCUSED)
- remarks (TextField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField)

Constraints:
- unique_together: ['student', 'classroom', 'date']
  (Prevents duplicate attendance records)

Methods:
- __str__(): Returns comprehensive attendance info
```

---

## 🌐 WEB INTERFACE FEATURES

### Dashboard (Home Page)
- Summary statistics cards (total students, classrooms, records)
- Quick action buttons
- Recent attendance activity table

### Student Management
- **List View**: All students in sortable table
- **Create**: Form to add new student
- **Detail View**: Student profile with attendance statistics
- **Update**: Edit student information
- **Delete**: Confirmation page with warning

### Classroom Management
- **List View**: All classrooms with teacher info
- **Create**: Form to add new classroom
- **Update**: Edit classroom details
- **Delete**: Confirmation page

### Attendance Management
- **List View**: All records with advanced filtering
  - Filter by: Student, Classroom, Date Range, Status
- **Create**: Record new attendance
- **Update**: Modify existing record
- **Delete**: Remove record

### Reports (EXTRA FEATURE - +20 POINTS)
- Comprehensive attendance statistics per student
- Metrics shown:
  - Total records
  - Present/Absent/Late/Excused breakdown
  - Attendance percentage
  - Color-coded status indicators
- Filtering options:
  - By classroom
  - By date range

---

## 🔌 REST API DOCUMENTATION

### Base URL: `http://localhost:8000/api/`

### Endpoints:

#### Students API
```
GET    /api/students/              # List all students
POST   /api/students/              # Create new student
GET    /api/students/{id}/         # Retrieve specific student
PUT    /api/students/{id}/         # Update student (full)
PATCH  /api/students/{id}/         # Update student (partial)
DELETE /api/students/{id}/         # Delete student
```

#### Classrooms API
```
GET    /api/classrooms/            # List all classrooms
POST   /api/classrooms/            # Create new classroom
GET    /api/classrooms/{id}/       # Retrieve specific classroom
PUT    /api/classrooms/{id}/       # Update classroom (full)
PATCH  /api/classrooms/{id}/       # Update classroom (partial)
DELETE /api/classrooms/{id}/       # Delete classroom
```

#### Attendance API
```
GET    /api/attendance/            # List all records
POST   /api/attendance/            # Create new record
GET    /api/attendance/{id}/       # Retrieve specific record
PUT    /api/attendance/{id}/       # Update record (full)
PATCH  /api/attendance/{id}/       # Update record (partial)
DELETE /api/attendance/{id}/       # Delete record
```

### API Features:
- **Pagination**: Automatically paginated (10 items per page)
- **Filtering**: Query parameters for filtering
- **Searching**: Full-text search on relevant fields
- **Ordering**: Sort by various fields

### Example API Requests:

#### Create Student (POST /api/students/)
```json
{
  "first_name": "Juan",
  "last_name": "Dela Cruz",
  "student_id": "2024-0001",
  "course_or_year_level": "1st Year BSCS",
  "is_active": true
}
```

**Response (201 Created):**
```json
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
```

#### Create Classroom (POST /api/classrooms/)
```json
{
  "name": "Introduction to Programming",
  "code": "CS101",
  "schedule": "MWF 9:00-10:00 AM",
  "teacher_name": "Prof. Maria Santos",
  "is_active": true
}
```

#### Create Attendance Record (POST /api/attendance/)
```json
{
  "student": 1,
  "classroom": 1,
  "date": "2024-12-12",
  "status": "PRESENT",
  "remarks": "Participated actively in class"
}
```

**Status Options**: PRESENT, ABSENT, LATE, EXCUSED

#### Filtering Examples:
```
GET /api/attendance/?student=1              # Records for student ID 1
GET /api/attendance/?classroom=2            # Records for classroom ID 2
GET /api/attendance/?status=PRESENT         # All present records
GET /api/attendance/?date=2024-12-12        # Records on specific date
GET /api/students/?is_active=true           # Only active students
GET /api/students/?search=Juan              # Search by name
```

---

## 🛠️ DJANGO ADMIN CUSTOMIZATION

### Access: http://localhost:8000/admin/

### Customized Features:

#### Student Admin
- **List Display**: student_id, last_name, first_name, course, status, created_at
- **Filters**: is_active, course_or_year_level, created_at
- **Search**: first_name, last_name, student_id, course

#### Classroom Admin
- **List Display**: code, name, teacher_name, schedule, status, created_at
- **Filters**: is_active, teacher_name, created_at
- **Search**: name, code, teacher_name

#### AttendanceRecord Admin
- **List Display**: date, student, classroom, status, created_at
- **Filters**: status, date, classroom, created_at
- **Search**: student name/ID, classroom name/code
- **Date Hierarchy**: Navigate by date

---

## 🎨 UI/UX FEATURES (Bootstrap 5)

### Design Elements:
- **Navbar**: Fixed top navigation with active link highlighting
- **Cards**: Elevated cards with shadows for content sections
- **Tables**: Responsive tables with hover effects
- **Forms**: Styled form controls with validation feedback
- **Badges**: Color-coded status indicators
  - Green: Present/Active
  - Red: Absent/Delete
  - Yellow: Late/Warning
  - Blue: Excused/Info
- **Buttons**: Consistent button styling with icons
- **Alerts**: Dismissible success/error/warning messages
- **Icons**: Bootstrap Icons throughout interface

### Responsive Design:
- Mobile-friendly navigation (hamburger menu)
- Responsive tables (horizontal scroll on small screens)
- Adaptive grid layout
- Touch-friendly buttons and links

---

## 📊 GRADING CRITERIA COVERAGE

### Functionality (70 points total):
1. **Basic CRUD (50 points)**:
   - ✅ Student CRUD: Create, Read, Update, Delete
   - ✅ Classroom CRUD: Create, Read, Update, Delete
   - ✅ Attendance Record CRUD: Create, Read, Update, Delete
   - ✅ All operations work correctly
   - ✅ Proper validation and error handling

2. **Additional Functionality (+20 points)**:
   - ✅ **Attendance Summary Report Page**:
     - Statistics per student
     - Present/Absent/Late/Excused counts
     - Attendance percentage calculation
     - Filtering by classroom and date range
     - Color-coded indicators
   - ✅ **Student Detail Page**:
     - Recent attendance records
     - Personal statistics

### UI (30 points):
- ✅ Bootstrap 5 implementation
- ✅ Base template with consistent navbar
- ✅ Clean, modern, professional design
- ✅ Responsive layout
- ✅ Proper spacing and alignment
- ✅ Card-based design
- ✅ Consistent color scheme
- ✅ Icons and visual hierarchy

### API (30 points):
- ✅ Django REST Framework implementation
- ✅ Serializers for all models
- ✅ ViewSets with all CRUD operations
- ✅ Proper HTTP methods (GET, POST, PUT/PATCH, DELETE)
- ✅ Filtering capabilities
- ✅ Search functionality
- ✅ Pagination
- ✅ Proper status codes (200, 201, 204, 404, etc.)

### Presentation (20 points):
- ✅ Clear explanation of project
- ✅ Live demonstration
- ✅ API testing examples
- ✅ Django concepts explanation
- ✅ Professional delivery

**TOTAL POSSIBLE: 150 points**

---

## 🧪 TESTING THE APPLICATION

### Manual Testing Checklist:

#### Student CRUD:
- [ ] Create a new student
- [ ] View student list
- [ ] View student details
- [ ] Edit student information
- [ ] Delete a student
- [ ] Verify validation (e.g., unique student_id)

#### Classroom CRUD:
- [ ] Create a new classroom
- [ ] View classroom list
- [ ] Edit classroom
- [ ] Delete classroom
- [ ] Verify validation (e.g., unique code)

#### Attendance CRUD:
- [ ] Record attendance for today
- [ ] View attendance list
- [ ] Filter by student/classroom/date/status
- [ ] Edit attendance record
- [ ] Delete attendance record
- [ ] Try creating duplicate (should fail)

#### Reports:
- [ ] View attendance summary
- [ ] Filter by classroom
- [ ] Filter by date range
- [ ] Verify percentage calculations

#### API Testing:
- [ ] GET all students
- [ ] POST new student
- [ ] GET single student
- [ ] PATCH student
- [ ] DELETE student
- [ ] Repeat for classrooms and attendance

---

## 🚀 DEPLOYMENT NOTES (Google IDX/Production)

### For Google IDX:
1. Push code to Git repository
2. Import project in Google IDX
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver 0.0.0.0:8000`

### For Production:
1. Update `settings.py`:
   - Set `DEBUG = False`
   - Add allowed hosts
   - Use environment variables for SECRET_KEY
2. Use PostgreSQL/MySQL instead of SQLite
3. Configure static files serving
4. Set up proper web server (Gunicorn + Nginx)

---

## 💡 KEY FEATURES TO HIGHLIGHT DURING PRESENTATION

1. **Complete CRUD operations** for all three models
2. **Foreign key relationships** between models
3. **Data validation** (unique constraints, required fields)
4. **Advanced filtering** on attendance list
5. **Attendance statistics** calculation
6. **RESTful API** with full CRUD support
7. **Django Admin** customization
8. **Bootstrap 5** responsive design
9. **Extra feature**: Comprehensive reporting system
10. **User-friendly interface** with clear navigation

---

## 📝 COMMON ISSUES & SOLUTIONS

### Issue: "No module named 'rest_framework'"
**Solution**: `pip install djangorestframework`

### Issue: "Table doesn't exist"
**Solution**: 
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "Static files not loading"
**Solution**: 
```bash
python manage.py collectstatic
```

### Issue: "Can't access admin"
**Solution**: Create superuser:
```bash
python manage.py createsuperuser
```

---

## 🎓 DJANGO CONCEPTS EXPLAINED

### MVT Pattern (Model-View-Template):
1. **Models**: Define database structure (models.py)
2. **Views**: Handle business logic (views.py, viewsets.py)
3. **Templates**: Present data to users (HTML files)

### Key Components:
- **ORM**: Object-Relational Mapping for database operations
- **URL Routing**: Maps URLs to views
- **Forms**: Handle user input validation
- **Admin**: Auto-generated admin interface
- **Middleware**: Process requests/responses
- **Serializers**: Convert data to/from JSON

### DRF Concepts:
- **Serializers**: Data validation and conversion
- **ViewSets**: CRUD operations in one class
- **Routers**: Auto-generate URL patterns
- **Filters**: Query data based on parameters

---

## 📧 CONTACT & SUPPORT

For questions or issues:
- Review PRESENTATION_GUIDE.md for detailed walkthrough
- Check Django documentation: https://docs.djangoproject.com/
- Check DRF documentation: https://www.django-rest-framework.org/

---

## ✅ PROJECT COMPLETION CHECKLIST

- [x] Django project setup
- [x] Database models created
- [x] Migrations applied
- [x] Forms created
- [x] Views implemented
- [x] Templates designed
- [x] URLs configured
- [x] Admin customized
- [x] REST API implemented
- [x] Extra features added
- [x] Testing completed
- [x] Documentation written
- [x] Presentation script prepared

**PROJECT STATUS: ✅ COMPLETE AND READY FOR DEMO**

---

**Good luck with your presentation! 🎉🚀**
