# REMAINING TEMPLATES - COPY THESE FILES

## classroom_list.html
```html
{% extends 'attendance/base.html' %}

{% block title %}Classrooms{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-6">
        <h1 class="h2"><i class="bi bi-building"></i> Classrooms</h1>
    </div>
    <div class="col-md-6 text-end">
        <a href="{% url 'classroom_create' %}" class="btn btn-success">
            <i class="bi bi-plus-circle"></i> Add New Classroom
        </a>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">All Classrooms ({{ classrooms.count }})</h5>
            </div>
            <div class="card-body">
                {% if classrooms %}
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-light">
                                <tr>
                                    <th>Code</th>
                                    <th>Name</th>
                                    <th>Schedule</th>
                                    <th>Teacher</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for classroom in classrooms %}
                                <tr>
                                    <td><strong>{{ classroom.code }}</strong></td>
                                    <td>{{ classroom.name }}</td>
                                    <td>{{ classroom.schedule }}</td>
                                    <td>{{ classroom.teacher_name }}</td>
                                    <td>
                                        {% if classroom.is_active %}
                                            <span class="badge bg-success">Active</span>
                                        {% else %}
                                            <span class="badge bg-secondary">Inactive</span>
                                        {% endif %}
                                    </td>
                                    <td>
                                        <a href="{% url 'classroom_update' classroom.pk %}" class="btn btn-sm btn-warning btn-action">
                                            <i class="bi bi-pencil"></i>
                                        </a>
                                        <a href="{% url 'classroom_delete' classroom.pk %}" class="btn btn-sm btn-danger btn-action">
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
                        No classrooms found. Click "Add New Classroom" to create one.
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## classroom_form.html
```html
{% extends 'attendance/base.html' %}

{% block title %}{{ action }} Classroom{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-12">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
                <li class="breadcrumb-item"><a href="{% url 'classroom_list' %}">Classrooms</a></li>
                <li class="breadcrumb-item active">{{ action }}</li>
            </ol>
        </nav>
        <h1 class="h2"><i class="bi bi-building"></i> {{ action }} Classroom</h1>
    </div>
</div>

<div class="row">
    <div class="col-lg-8 col-md-10 mx-auto">
        <div class="card">
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.name.id_for_label }}" class="form-label">Class Name *</label>
                        {{ form.name }}
                        {% if form.name.errors %}
                            <div class="text-danger small">{{ form.name.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.code.id_for_label }}" class="form-label">Class Code *</label>
                        {{ form.code }}
                        {% if form.code.errors %}
                            <div class="text-danger small">{{ form.code.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.schedule.id_for_label }}" class="form-label">Schedule *</label>
                        {{ form.schedule }}
                        {% if form.schedule.errors %}
                            <div class="text-danger small">{{ form.schedule.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.teacher_name.id_for_label }}" class="form-label">Teacher Name *</label>
                        {{ form.teacher_name }}
                        {% if form.teacher_name.errors %}
                            <div class="text-danger small">{{ form.teacher_name.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3 form-check">
                        {{ form.is_active }}
                        <label for="{{ form.is_active.id_for_label }}" class="form-check-label">Active Classroom</label>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'classroom_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-primary">Save Classroom</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## classroom_confirm_delete.html
```html
{% extends 'attendance/base.html' %}

{% block title %}Delete Classroom{% endblock %}

{% block content %}
<div class="row">
    <div class="col-lg-6 col-md-8 mx-auto">
        <div class="card border-danger">
            <div class="card-header bg-danger text-white">
                <h5 class="mb-0">Confirm Deletion</h5>
            </div>
            <div class="card-body">
                <p>Are you sure you want to delete this classroom?</p>
                <dl class="row">
                    <dt class="col-sm-4">Code:</dt>
                    <dd class="col-sm-8">{{ classroom.code }}</dd>
                    <dt class="col-sm-4">Name:</dt>
                    <dd class="col-sm-8">{{ classroom.name }}</dd>
                </dl>
                <div class="alert alert-warning">
                    This will also delete all attendance records for this classroom.
                </div>
                <form method="post">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'classroom_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-danger">Yes, Delete</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

Save this file and I'll create the attendance templates next.
