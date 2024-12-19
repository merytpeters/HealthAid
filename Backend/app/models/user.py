from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db

class User(db.Model):
    """User model to represent a user in the system."""

    # Define the columns for the User table
    id = db.Column(db.Integer, primary_key=True)  # User ID
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email
    password_hash = db.Column(db.String(128), nullable=False)  # Password hash

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """Hash the password and store it in the database."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)
