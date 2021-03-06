"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, jsonify, redirect, url_for
from webapp import app, db
from webapp.models import Task
from webapp.forms import TaskForm
from datetime import *

def is_assigned(task, assignee):
    return task.name.lower() == assignee.lower()

def is_due(task):
    
    if task.deadline and date.today() < task.deadline:
        return False
    return True 

# http://localhost:5000/tasks
@app.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    tasksdue = [(task, is_due(task)) for task in tasks]
    return render_template("tasks.html", tasksdue=tasksdue)

@app.route('/tasks/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm(request.form)
    if "name" in request.form:
        print (form.deadline.data)
        db.session.add(Task(form.name.data, False, form.deadline.data))
        db.session.commit()
        return redirect(url_for("get_tasks"))
    return render_template("add_task.html", form=form)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
