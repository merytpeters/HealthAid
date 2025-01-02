from flask import Blueprint, request, jsonify
from app.db import db
from app.models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Initialize Blueprint
auth_bp = Blueprint('auth', __name__)

# Signup route for user registration
@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        # Validate incoming data
        required_fields = ['first_name', 'last_name', 'email', 'password', 'gender', 'weight', 'height', 'username']
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Missing required fields"}), 400

        # Check if user already exists by email
        if User.query.filter_by(email=data['email']).first():
            return jsonify({"message": "User with this email already exists"}), 400

        # Check if user already exists by username
        if User.query.filter_by(username=data['username']).first():
            return jsonify({"message": "Username already taken"}), 400

        # Create a new user and hash the password
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['username'],
            date_of_birth=data.get('date_of_birth', None),
            gender=data['gender'],
            weight=data['weight'],
            height=data['height']
        )
        new_user.set_password(data['password'])  # Set hashed password
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Login route for user authentication
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        # Validate incoming data
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"message": "Missing required fields"}), 400

        # Find the user by email
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            return jsonify({"message": "Invalid email or password"}), 401

        # Check if the password is correct
        if user.check_password(data['password']):
            user_id_str = str(user.id)
            access_token = create_access_token(identity=user_id_str)

            return jsonify({
                "message": "Login successful",
                "access_token": access_token
            }), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Logout route for invalidating the token (client-side)
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()  # Protect the route, requiring a valid token to log out
def logout():
    try:
        current_user = get_jwt_identity()  # Get the user identity (e.g., user id)
        print(f"DEBUG: Current user: {current_user}")  # Log the current user identity

        if not isinstance(current_user, str):
            raise ValueError("The user identity is not a string.")

        # Here we just inform the client to delete the token locally
        return jsonify({"message": "Successfully logged out"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Profile route to view the user's profile (requires authentication)
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()  # Protect the route
def profile():
    try:
        user_id = get_jwt_identity()  # Get the user ID from the JWT token
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        return jsonify({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "gender": user.gender,
            "weight": user.weight,
            "height": user.height
        }), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# Register the blueprint in the app
def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
