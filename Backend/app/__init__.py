#!/usr/bin/env python3
"""Database Initialization with an instance of Flask app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def create_app():
    """Database mapping with flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app