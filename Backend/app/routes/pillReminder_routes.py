from flask import Blueprint, request, jsonify
from app import db
from app.models.pillReminder import PillReminder
from datetime import datetime
from flask_mail import Message
from app import mail  # Ensure mail is correctly imported

pill_reminder_bp = Blueprint('pill_reminder', __name__)

# Route to add a new pill reminder
@pill_reminder_bp.route('/add_reminder', methods=['POST'])
def add_pill_reminder():
    data = request.get_json()

    # Validate required fields
    drug_name = data.get('drug_name')
    pill_time = data.get('pill_time')
    dosage = data.get('dosage')
    email_notification = data.get('email_notification', False)

    # Debugging: Print received data for debugging purposes
    print(f"Received data: {data}")

    if not drug_name or not pill_time or not dosage:
        return jsonify({"message": "Missing required fields"}), 400

    # Convert pill_time string to time object
    try:
        pill_time = datetime.strptime(pill_time, "%H:%M:%S").time()
    except ValueError:
        return jsonify({"message": "Invalid time format. Please use HH:MM:SS."}), 400

    # Create a new reminder entry
    new_reminder = PillReminder(
        drug_name=drug_name,
        pill_time=pill_time,
        dosage=dosage,
        email_notification=email_notification
    )

    # Add to the database
    try:
        db.session.add(new_reminder)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred while saving the reminder: {str(e)}"}), 500

    return jsonify({"message": "Pill reminder added successfully!"}), 201

# Route to view all pill reminders
@pill_reminder_bp.route('/view_reminders', methods=['GET'])
def view_pill_reminders():
    reminders = PillReminder.query.all()
    reminders_list = [
        {
            'id': reminder.id,
            'drug_name': reminder.drug_name,
            'dosage': reminder.dosage,
            'pill_time': str(reminder.pill_time),
            'email_notification': reminder.email_notification
        }
        for reminder in reminders
    ]
    return jsonify(reminders_list), 200

# Route to send a pill reminder notification
@pill_reminder_bp.route('/send_notification/<int:id>', methods=['POST'])
def send_notification(id):
    reminder = PillReminder.query.get_or_404(id)

    # If email notification is enabled, send it
    if reminder.email_notification:
        send_email_notification(reminder)
        return jsonify({"message": f"Notification sent for {reminder.drug_name}."}), 200
    else:
        return jsonify({"message": "Email notification is not enabled for this reminder."}), 400

def send_email_notification(reminder):
    """Send email notification for pill reminder"""
    try:
        msg = Message(
            f"Time to take your {reminder.drug_name}",
            recipients=["isahabdulsalam03@gmail.com"],  # Change to the user's email or make it dynamic
            body=f"Hello, it's time to take your {reminder.dosage} of {reminder.drug_name}."
        )
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
