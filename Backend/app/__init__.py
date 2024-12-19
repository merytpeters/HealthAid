#!/usr/bin/env python3
"""Database Initialization with an instance of Flask app"""
from flask import Flask
from flask_migrate import Migrate
from config import Config
from .db import db
from .routes.auth import auth_bp
from .routes.healthInventory_routes import inventory_bp



migrate = Migrate()

def create_app():
    """Database mapping with flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    return app
