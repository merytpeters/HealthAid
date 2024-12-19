# app/routes/__init__.py

from flask import Blueprint, request, jsonify
from app.db import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)


# Signup route for user registration
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Validate incoming data
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    # Check if user already exists by email or username
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User with this email already exists"}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already taken"}), 400

    # Create a new user and hash the password
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])  # Set hashed password
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

# Login route for user authentication
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate incoming data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    # Find the user by email
    user = User.query.filter_by(email=data['email']).first()

    # Check if user exists and if the password is correct
    if not user or not user.check_password(data['password']):
        return jsonify({"message": "Invalid email or password"}), 401

    # Create a JWT token for the authenticated user
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200

# Profile route to view the user's profile (requires authentication)
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()  # Get the user ID from the JWT token
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "username": user.username,
        "email": user.email
    }), 200

# Function to register blueprints with the app

# The function below is commented out for consistency as all routes will
# be registered in the app/__init__.py def create_app() entry point
# def register_blueprints(app):
    # app.register_blueprint(auth_bp, url_prefix='/auth')
