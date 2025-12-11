# ATTENDANCE AND REPORT TEMPLATES

## attendance_list.html
```html
{% extends 'attendance/base.html' %}

{% block title %}Attendance Records{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-6">
        <h1 class="h2"><i class="bi bi-clipboard-check"></i> Attendance Records</h1>
    </div>
    <div class="col-md-6 text-end">
        <a href="{% url 'attendance_create' %}" class="btn btn-success">
            <i class="bi bi-clipboard-plus"></i> Record Attendance
        </a>
    </div>
</div>

<div class="row mb-4">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">Filter Records</h5>
            </div>
            <div class="card-body">
                <form method="get" class="row g-3">
                    <div class="col-md-3">
                        <label class="form-label">Student</label>
                        {{ filter_form.student }}
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Classroom</label>
                        {{ filter_form.classroom }}
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Date From</label>
                        {{ filter_form.date_from }}
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Date To</label>
                        {{ filter_form.date_to }}
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Status</label>
                        {{ filter_form.status }}
                    </div>
                    <div class="col-12">
                        <button type="submit" class="btn btn-primary">
                            <i class="bi bi-funnel"></i> Apply Filters
                        </button>
                        <a href="{% url 'attendance_list' %}" class="btn btn-secondary">
                            <i class="bi bi-x-circle"></i> Clear
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">All Records ({{ records.count }})</h5>
            </div>
            <div class="card-body">
                {% if records %}
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-light">
                                <tr>
                                    <th>Date</th>
                                    <th>Student</th>
                                    <th>Class</th>
                                    <th>Status</th>
                                    <th>Remarks</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for record in records %}
                                <tr>
                                    <td>{{ record.date|date:"M d, Y" }}</td>
                                    <td>
                                        <a href="{% url 'student_detail' record.student.pk %}">
                                            {{ record.student.student_id }} - {{ record.student.get_full_name }}
                                        </a>
                                    </td>
                                    <td>{{ record.classroom.code }} - {{ record.classroom.name }}</td>
                                    <td>
                                        {% if record.status == 'PRESENT' %}
                                            <span class="badge bg-success">{{ record.get_status_display }}</span>
                                        {% elif record.status == 'ABSENT' %}
                                            <span class="badge bg-danger">{{ record.get_status_display }}</span>
                                        {% elif record.status == 'LATE' %}
                                            <span class="badge bg-warning text-dark">{{ record.get_status_display }}</span>
                                        {% else %}
                                            <span class="badge bg-info">{{ record.get_status_display }}</span>
                                        {% endif %}
                                    </td>
                                    <td>{{ record.remarks|default:"-"|truncatewords:10 }}</td>
                                    <td>
                                        <a href="{% url 'attendance_update' record.pk %}" class="btn btn-sm btn-warning btn-action">
                                            <i class="bi bi-pencil"></i>
                                        </a>
                                        <a href="{% url 'attendance_delete' record.pk %}" class="btn btn-sm btn-danger btn-action">
                                            <i class="bi bi-trash"></i>
                                        </a>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                {% else %}
                    <div class="alert alert-info mb-0">
                        No attendance records found.
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## attendance_form.html
```html
{% extends 'attendance/base.html' %}

{% block title %}{{ action }} Attendance{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
                <li class="breadcrumb-item"><a href="{% url 'attendance_list' %}">Attendance</a></li>
                <li class="breadcrumb-item active">{{ action }}</li>
            </ol>
        </nav>
        <h1 class="h2"><i class="bi bi-clipboard-check"></i> {{ action }} Attendance Record</h1>
    </div>
</div>

<div class="row">
    <div class="col-lg-8 col-md-10 mx-auto">
        <div class="card">
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.student.id_for_label }}" class="form-label">Student *</label>
                        {{ form.student }}
                        {% if form.student.errors %}
                            <div class="text-danger small">{{ form.student.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.classroom.id_for_label }}" class="form-label">Classroom *</label>
                        {{ form.classroom }}
                        {% if form.classroom.errors %}
                            <div class="text-danger small">{{ form.classroom.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.date.id_for_label }}" class="form-label">Date *</label>
                        {{ form.date }}
                        {% if form.date.errors %}
                            <div class="text-danger small">{{ form.date.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.status.id_for_label }}" class="form-label">Status *</label>
                        {{ form.status }}
                        {% if form.status.errors %}
                            <div class="text-danger small">{{ form.status.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.remarks.id_for_label }}" class="form-label">Remarks</label>
                        {{ form.remarks }}
                        {% if form.remarks.errors %}
                            <div class="text-danger small">{{ form.remarks.errors }}</div>
                        {% endif %}
                    </div>
                    
                    {% if form.non_field_errors %}
                        <div class="alert alert-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'attendance_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-primary">Save Record</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## attendance_confirm_delete.html
```html
{% extends 'attendance/base.html' %}

{% block title %}Delete Attendance Record{% endblock %}

{% block content %}
<div class="row">
    <div class="col-lg-6 col-md-8 mx-auto">
        <div class="card border-danger">
            <div class="card-header bg-danger text-white">
                <h5 class="mb-0">Confirm Deletion</h5>
            </div>
            <div class="card-body">
                <p>Are you sure you want to delete this attendance record?</p>
                <dl class="row">
                    <dt class="col-sm-4">Date:</dt>
                    <dd class="col-sm-8">{{ record.date|date:"F d, Y" }}</dd>
                    <dt class="col-sm-4">Student:</dt>
                    <dd class="col-sm-8">{{ record.student.get_full_name }}</dd>
                    <dt class="col-sm-4">Class:</dt>
                    <dd class="col-sm-8">{{ record.classroom.code }}</dd>
                    <dt class="col-sm-4">Status:</dt>
                    <dd class="col-sm-8">{{ record.get_status_display }}</dd>
                </dl>
                <form method="post">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'attendance_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-danger">Yes, Delete</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## report.html (EXTRA FEATURE - +20 POINTS)
```html
{% extends 'attendance/base.html' %}

{% block title %}Attendance Report{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <h1 class="h2"><i class="bi bi-graph-up"></i> Attendance Summary Report</h1>
        <p class="text-muted">Comprehensive attendance statistics for all students</p>
    </div>
</div>

<div class="row mb-4">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">Filter Report</h5>
            </div>
            <div class="card-body">
                <form method="get" class="row g-3">
                    <div class="col-md-4">
                        <label class="form-label">Filter by Classroom</label>
                        <select name="classroom" class="form-select">
                            <option value="">All Classrooms</option>
                            {% for classroom in classrooms %}
                                <option value="{{ classroom.id }}" {% if classroom.id|stringformat:"s" == selected_classroom %}selected{% endif %}>
                                    {{ classroom.code }} - {{ classroom.name }}
                                </option>
                            {% endfor %}
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Date From</label>
                        <input type="date" name="date_from" class="form-control" value="{{ date_from }}">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Date To</label>
                        <input type="date" name="date_to" class="form-control" value="{{ date_to }}">
                    </div>
                    <div class="col-md-2 d-flex align-items-end">
                        <button type="submit" class="btn btn-primary w-100">Apply</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">Student Attendance Statistics</h5>
            </div>
            <div class="card-body">
                {% if student_stats %}
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-light">
                                <tr>
                                    <th>Student ID</th>
                                    <th>Name</th>
                                    <th>Course/Year</th>
                                    <th>Total Records</th>
                                    <th>Present</th>
                                    <th>Absent</th>
                                    <th>Late</th>
                                    <th>Excused</th>
                                    <th>Attendance %</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for stat in student_stats %}
                                <tr>
                                    <td>
                                        <a href="{% url 'student_detail' stat.student.pk %}">
                                            {{ stat.student.student_id }}
                                        </a>
                                    </td>
                                    <td>{{ stat.student.get_full_name }}</td>
                                    <td>{{ stat.student.course_or_year_level }}</td>
                                    <td><strong>{{ stat.total }}</strong></td>
                                    <td><span class="badge bg-success">{{ stat.present }}</span></td>
                                    <td><span class="badge bg-danger">{{ stat.absent }}</span></td>
                                    <td><span class="badge bg-warning text-dark">{{ stat.late }}</span></td>
                                    <td><span class="badge bg-info">{{ stat.excused }}</span></td>
                                    <td>
                                        {% if stat.percentage >= 75 %}
                                            <strong class="text-success">{{ stat.percentage }}%</strong>
                                        {% elif stat.percentage >= 50 %}
                                            <strong class="text-warning">{{ stat.percentage }}%</strong>
                                        {% else %}
                                            <strong class="text-danger">{{ stat.percentage }}%</strong>
                                        {% endif %}
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="alert alert-info mt-3">
                        <strong>Legend:</strong> 
                        <span class="text-success">Green (≥75%)</span> = Good attendance | 
                        <span class="text-warning">Yellow (50-74%)</span> = Needs improvement | 
                        <span class="text-danger">Red (<50%)</span> = At risk
                    </div>
                {% else %}
                    <div class="alert alert-info mb-0">
                        No attendance data available for the selected filters.
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
```
