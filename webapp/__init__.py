"""
The flask application package.
"""
import os

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'postgresql+psycopg2://postgres:example@localhost/todo')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# initialize the database connection

db = SQLAlchemy(app)


import webapp.views
import webapp.models

# initialize database migration management
migrate = Migrate(app, db)
