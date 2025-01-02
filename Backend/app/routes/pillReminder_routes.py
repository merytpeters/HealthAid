from flask import Blueprint, request, jsonify
from app import db
from app.models.pillReminder import PillReminder
from datetime import datetime
from werkzeug.exceptions import NotFound
from flask_mail import Message

pill_reminder_bp = Blueprint('pill_reminder', __name__)

# Route to send notification
@pill_reminder_bp.route('/send_notification/<int:id>', methods=['POST'])
def send_notification(id):
    reminder = PillReminder.query.get(id)
    if reminder:
        if reminder.user:  # Ensure reminder has a user before trying to send the email
            send_email_notification(reminder)
            return jsonify({"message": f"Notification sent for {reminder.drug_name}."}), 200
        else:
            return jsonify({"error": "No associated user found for this pill reminder."}), 404
    return jsonify({"error": "Pill reminder not found."}), 404

def send_email_notification(reminder):
    try:
        # Import mail inside the function to avoid circular import
        from app import mail

        # Ensure reminder has a valid user and user has an email
        if reminder.user and reminder.user.email:
            msg = Message('Pill Reminder', recipients=[reminder.user.email])
            msg.body = f"Reminder to take your medication: {reminder.drug_name} at {reminder.pill_time}."
            mail.send(msg)
        else:
            # Handle case where user does not have a valid email or is missing
            print("User does not have a valid email or is missing.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Route to update a pill reminder
@pill_reminder_bp.route('/update_reminder/<int:id>', methods=['PUT'])
def update_pill_reminder(id):
    try:
        reminder = PillReminder.query.get(id)
        if not reminder:
            raise NotFound("Pill reminder not found.")

        data = request.get_json()
        drug_name = data.get('drug_name')
        pill_time = data.get('pill_time')
        dosage = data.get('dosage')
        email_notification = data.get('email_notification', reminder.email_notification)

        if drug_name:
            reminder.drug_name = drug_name
        if pill_time:
            try:
                reminder.pill_time = datetime.strptime(pill_time, "%H:%M:%S").time()
            except ValueError:
                return jsonify({"message": "Invalid time format. Please use HH:MM:SS."}), 400
        if dosage:
            reminder.dosage = dosage
        reminder.email_notification = email_notification

        db.session.commit()
        return jsonify({"message": "Pill reminder updated successfully!"}), 200
    except NotFound as e:
        return jsonify({"error": str(e).split(": ", 1)[1]}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while updating the reminder: {str(e)}"}), 500

# Route to view all pill reminders
@pill_reminder_bp.route('/view_reminders', methods=['GET'])
def view_reminders():
    try:
        reminders = PillReminder.query.all()
        if not reminders:
            return jsonify({"message": "No pill reminders found."}), 404

        reminders_list = [
            {
                "id": reminder.id,
                "drug_name": reminder.drug_name,
                "pill_time": str(reminder.pill_time),
                "dosage": reminder.dosage,
                "email_notification": reminder.email_notification
            }
            for reminder in reminders
        ]
        return jsonify({"reminders": reminders_list}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred while retrieving the reminders: {str(e)}"}), 500

# Route to add a pill reminder
@pill_reminder_bp.route('/add_reminder', methods=['POST'])
def add_reminder():
    try:
        # Get the data from the request
        data = request.get_json()

        # Validate the input data
        if not data.get('drug_name') or not data.get('pill_time') or not data.get('dosage') or not data.get('user_id'):
            return jsonify({"error": "Missing required fields: drug_name, pill_time, dosage, or user_id."}), 400

        # Convert pill_time to a datetime object
        try:
            pill_time = datetime.strptime(data['pill_time'], "%H:%M:%S").time()
        except ValueError:
            return jsonify({"error": "Invalid time format. Please use HH:MM:SS."}), 400

        # Create a new pill reminder object
        reminder = PillReminder(
            drug_name=data['drug_name'],
            pill_time=pill_time,
            dosage=data['dosage'],
            email_notification=data.get('email_notification', False),
            user_id=data['user_id']
        )

        # Add to the session and commit
        db.session.add(reminder)
        db.session.commit()

        return jsonify({"message": "Pill reminder added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while adding the reminder: {str(e)}"}), 500
