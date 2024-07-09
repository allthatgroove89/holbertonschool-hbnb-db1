""" This module is responsible for selecting the repository
to be used based on the environment variable REPOSITORY_ENV_VAR."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
