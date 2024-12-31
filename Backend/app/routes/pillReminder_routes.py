from flask import Blueprint, request, jsonify
from app import db
from app.models.pillReminder import PillReminder
from datetime import datetime
from werkzeug.exceptions import NotFound

pill_reminder_bp = Blueprint('pill_reminder', __name__)

# Route to send notification
@pill_reminder_bp.route('/send_notification/<int:id>', methods=['POST'])
def send_notification(id):
    reminder = PillReminder.query.get(id)
    if reminder:
        send_email_notification(reminder)
        return jsonify({"message": f"Notification sent for {reminder.drug_name}."}), 200
    return jsonify({"error": "Pill reminder not found."}), 404

def send_email_notification(reminder):
    from app import mail
    from flask_mail import Message

    msg = Message('Pill Reminder', 
                  recipients=[reminder.user.email])
    msg.body = f"Reminder to take your medication: {reminder.drug_name} at {reminder.pill_time}."
    mail.send(msg)

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
