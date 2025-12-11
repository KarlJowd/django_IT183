# 🎓 STUDENT ATTENDANCE TRACKER - QUICK START GUIDE

## 🚀 Server is Running!
**Access the application at:** http://127.0.0.1:8000/

---

## 🔑 ADMIN CREDENTIALS
- **Username:** `admin`
- **Password:** `admin123`
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## 📍 MAIN WEB PAGES

### Home & Dashboard
- **Home/Dashboard:** http://127.0.0.1:8000/

### Student Management
- **Student List:** http://127.0.0.1:8000/students/
- **Add Student:** http://127.0.0.1:8000/students/create/
- **View Student:** http://127.0.0.1:8000/students/<id>/
- **Edit Student:** http://127.0.0.1:8000/students/<id>/update/
- **Delete Student:** http://127.0.0.1:8000/students/<id>/delete/

### Classroom Management
- **Classroom List:** http://127.0.0.1:8000/classrooms/
- **Add Classroom:** http://127.0.0.1:8000/classrooms/create/
- **Edit Classroom:** http://127.0.0.1:8000/classrooms/<id>/update/
- **Delete Classroom:** http://127.0.0.1:8000/classrooms/<id>/delete/

### Attendance Management
- **Attendance List:** http://127.0.0.1:8000/attendance/
- **Mark Attendance:** http://127.0.0.1:8000/attendance/create/
- **Edit Attendance:** http://127.0.0.1:8000/attendance/<id>/update/
- **Delete Attendance:** http://127.0.0.1:8000/attendance/<id>/delete/

### Reports (Extra Feature)
- **Attendance Report:** http://127.0.0.1:8000/reports/

---

## 🔌 API ENDPOINTS

### Base API URL: http://127.0.0.1:8000/api/

### Students API
- **List/Create:** GET/POST http://127.0.0.1:8000/api/students/
- **Retrieve/Update/Delete:** GET/PUT/PATCH/DELETE http://127.0.0.1:8000/api/students/<id>/

### Classrooms API
- **List/Create:** GET/POST http://127.0.0.1:8000/api/classrooms/
- **Retrieve/Update/Delete:** GET/PUT/PATCH/DELETE http://127.0.0.1:8000/api/classrooms/<id>/

### Attendance API
- **List/Create:** GET/POST http://127.0.0.1:8000/api/attendance/
- **Retrieve/Update/Delete:** GET/PUT/PATCH/DELETE http://127.0.0.1:8000/api/attendance/<id>/

---

## 📝 SAMPLE API REQUESTS

### Create a Student (POST to http://127.0.0.1:8000/api/students/)
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "student_id": "STU001",
    "course_or_year_level": "Year 3",
    "is_active": true
}
```

### Create a Classroom (POST to http://127.0.0.1:8000/api/classrooms/)
```json
{
    "name": "Introduction to Programming",
    "code": "CS101",
    "schedule": "MWF 10:00-11:30 AM",
    "teacher_name": "Prof. Smith",
    "is_active": true
}
```

### Mark Attendance (POST to http://127.0.0.1:8000/api/attendance/)
```json
{
    "student": 1,
    "classroom": 1,
    "date": "2024-12-12",
    "status": "PRESENT",
    "remarks": "On time"
}
```

**Status Options:** `PRESENT`, `ABSENT`, `LATE`, `EXCUSED`

---

## ✅ QUICK TESTING WORKFLOW

### 1. Login to Admin Panel
- Go to http://127.0.0.1:8000/admin/
- Login with admin/admin123
- Explore the customized admin interface

### 2. Add Test Data via Web Interface
- Navigate to http://127.0.0.1:8000/
- Click "Add Student" and create 2-3 students
- Click "Add Classroom" and create 1-2 classrooms
- Click "Mark Attendance" and create several attendance records

### 3. Test Filtering
- Go to Attendance page
- Use filter form to filter by student, classroom, status, date range

### 4. View Reports (Extra Feature)
- Navigate to Reports page
- Filter by classroom or date range
- View attendance statistics and percentages

### 5. Test API with Browser/Postman
- Open http://127.0.0.1:8000/api/ in browser to see API root
- Test GET requests to list endpoints
- Use Postman to test POST/PUT/DELETE operations

---

## 🎯 GRADING REQUIREMENTS COVERAGE

### ✅ Functionality (70 points)
- [x] Student CRUD (Create, Read, Update, Delete)
- [x] Classroom CRUD
- [x] Attendance Record CRUD
- [x] All models have relationships (ForeignKey)
- [x] Form validation and error handling
- [x] Django admin customization

### ✅ Extra Feature (+20 bonus points)
- [x] Attendance Report with statistics
- [x] Filtering by classroom and date range
- [x] Attendance percentage calculations
- [x] Color-coded attendance rates

### ✅ UI Design (30 points)
- [x] Bootstrap 5 responsive design
- [x] Professional navbar and footer
- [x] Card-based layouts
- [x] Status badges with colors
- [x] Icons from Bootstrap Icons
- [x] Responsive tables and forms

### ✅ API (30 points)
- [x] Django REST Framework implementation
- [x] Full CRUD for all 3 models
- [x] Filtering, search, ordering
- [x] Pagination (10 items per page)
- [x] Nested serializers
- [x] API validation

### ✅ Presentation (20 points)
- [x] See PRESENTATION_GUIDE.md for demo script
- [x] Working example ready to demonstrate
- [x] Test data can be easily created

---

## 🛠️ USEFUL COMMANDS

### Run Server
```bash
cd C:\Users\admin\Documents\Codes\attendance_system
.\venv\Scripts\python.exe manage.py runserver
```

### Create Database Backup
```bash
copy db.sqlite3 db.backup.sqlite3
```

### Restart Server
- Press `CTRL+C` in terminal
- Run the server command again

### View Migration History
```bash
.\venv\Scripts\python.exe manage.py showmigrations
```

---

## 📚 DOCUMENTATION FILES
- **README.md** - Complete project documentation
- **PRESENTATION_GUIDE.md** - Detailed demo script with timing
- **requirements.txt** - Python dependencies

---

## 🐛 TROUBLESHOOTING

### Server Not Running?
Check terminal output for errors. Server should show:
```
Starting development server at http://127.0.0.1:8000/
```

### Page Not Found?
Verify you're using the correct URL from the list above.

### API Returns Empty Lists?
Create test data first through the web interface or admin panel.

### Form Validation Errors?
- Student ID must be unique
- Classroom code must be unique
- Cannot mark duplicate attendance (same student, classroom, date)

---

## 🎉 YOU'RE ALL SET!

The complete Student Attendance Tracker is now running and ready for demonstration.

**Total Score Potential:** 150 points (70 + 20 bonus + 30 + 30)

Good luck with your presentation! 🚀
