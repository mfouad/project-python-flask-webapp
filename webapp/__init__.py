"""
The flask application package.
"""
import os

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:example@db/todo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# initialize the database connection

db = SQLAlchemy(app)
db.create_all()
# initialize database migration management
migrate = Migrate(app, db)


import webapp.views
import webapp.models
