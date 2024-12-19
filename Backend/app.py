import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# Initialize the SQLAlchemy instance globally
db = SQLAlchemy()

# Ensure the Backend directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    app = Flask(__name__)
    
    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthaid.db'  # example for SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance reasons

    # Initialize the app with the database
    db.init_app(app)

    # Import and register blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app

# Entry point to run the Flask app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
