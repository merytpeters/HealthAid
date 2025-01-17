#!/usr/bin/env python3

import logging
import os
import sys

# Set logging level to WARNING for most of the app
logging.basicConfig(level=logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.INFO)  # To show only required werkzeug logs

logger = logging.getLogger(__name__)

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
from app.routes.dashboard_routes import dashboard_bp
# from app.routes.symptomChecker_routes import symptom_checker_bp
from app.routes.symptomChecker_routes import symptom_checker_bp
from app.routes.drug_interaction_checker_routes import drug_interaction_checker_bp
from flask_cors import CORS

# Initialize extensions
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app():
    """Database mapping with flask app"""
    app = Flask(__name__)

    # Load the configuration from the Config class in config.py
    app.config.from_object(Config)

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)

    # Enables CORS for the frontend URL

    CORS(app, origins=["https://localhost:3000"], supports_credentials=True)

    # Register blueprints for the routes
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(pill_reminder_bp, url_prefix='/pill_reminder')
    app.register_blueprint(first_aid_bp, url_prefix='/first_aid')
    app.register_blueprint(medical_journal_bp, url_prefix='/medical_journal')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    #app.register_blueprint(symptom_checker_bp, url_prefix='/symptom_checker')
    app.register_blueprint(drug_interaction_checker_bp, url_prefix='/drug_interaction_checker')

    return app
