#!/usr/bin/env python3
"""Database Initialization with an instance of Flask app"""

from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from app.db import db
from app.models.users import User
from app.routes.auth import auth_bp
from app.routes.healthInventory_routes import inventory_bp
from app.routes.pillReminder_routes import pill_reminder_bp
from app.routes.first_aid_guide_routes import first_aid_bp
from app.routes.medicalJournal_routes import medical_journal_bp

# Initialize extensions
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """Database mapping with flask app"""
    app = Flask(__name__)

    # Load the configuration from the Config class in config.py
    app.config.from_object(Config)

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    mail = Mail(app)
    jwt.init_app(app)

    # Register blueprints for the routes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(pill_reminder_bp, url_prefix='/pill_reminder')
    app.register_blueprint(first_aid_bp, url_prefix='/first_aid')
    app.register_blueprint(medical_journal_bp, url_prefix='/medical_journal')

    return app
