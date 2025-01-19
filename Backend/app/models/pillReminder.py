from app.db import db
from datetime import datetime

class PillReminder(db.Model):
    __tablename__ = 'pill_reminder'

    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String(255), nullable=False)
    pill_time = db.Column(db.Time, nullable=False)
    dosage = db.Column(db.String(100), nullable=False)

    missed_pills = db.Column(db.Integer, default=0)
    taken_pills = db.Column(db.Integer, default=0)

    email_notification = db.Column(db.Boolean, default=False)

    # Foreign key relationship to the users table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship with the User model
    user = db.relationship('User', backref=db.backref('pill_reminders', lazy=True))

    def __init__(self, drug_name, pill_time, dosage, email_notification, user_id):
        """Initialize a new pill reminder."""
        self.drug_name = drug_name
        self.pill_time = pill_time
        self.dosage = dosage
        self.email_notification = email_notification
        self.user_id = user_id

    def mark_taken(self, quantity):
        """Marks a certain quantity of pills as taken."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.taken_pills += quantity

    def mark_missed(self, quantity):
        """Marks a certain quantity of pills as missed."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.missed_pills += quantity
