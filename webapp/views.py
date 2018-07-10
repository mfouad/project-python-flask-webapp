"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, jsonify
from webapp import app, models



# http://localhost:5555/tasks
@app.route('/tasks')
def get_tasks():
    tasks = [
        Task('Python', True),
        Task('Flask', True),
        Task('Docker', False)
    ]
    return ",".join([task.name for task in tasks])

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
