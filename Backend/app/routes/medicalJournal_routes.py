from flask import Blueprint, request, jsonify
from app import db
from app.models.symptomCard import SymptomCard
from datetime import datetime

# Define the blueprint
medical_journal_bp = Blueprint('medical_journal', __name__)

# Route to add a new symptom card
@medical_journal_bp.route('/add_symptom', methods=['POST'])
def add_symptom():
    data = request.get_json()
    timestamp = data.get('timestamp')
    symptoms = data.get('symptoms')

    if not symptoms:
        return jsonify({"message": "Symptoms field is required"}), 400

    try:
        timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") if timestamp else datetime.utcnow()
    except ValueError:
        return jsonify({"message": "Invalid timestamp format. Please use YYYY-MM-DD HH:MM:SS."}), 400

    new_symptom = SymptomCard(timestamp=timestamp, symptoms=symptoms)

    try:
        db.session.add(new_symptom)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

    return jsonify({"message": "Symptom card added successfully!"}), 201

# Route to get all symptom cards
@medical_journal_bp.route('/get_symptoms', methods=['GET'])
def get_symptoms():
    symptoms = SymptomCard.query.all()
    symptoms_list = [
        {
            'id': symptom.id,
            'timestamp': symptom.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'symptoms': symptom.symptoms
        }
        for symptom in symptoms
    ]
    return jsonify(symptoms_list), 200

# Route to update a symptom card
@medical_journal_bp.route('/update_symptom/<int:id>', methods=['PUT'])
def update_symptom(id):
    try:
        # Try to get the symptom card by ID, return 404 if not found
        symptom = SymptomCard.query.get(id)

        if not symptom:
            return jsonify({"error": "Symptom card not found"}), 404

        # Get the new symptom data from the request
        data = request.get_json()
        symptoms = data.get('symptoms')

        if not symptoms:
            return jsonify({"message": "Symptoms field is required"}), 400

        # Update the symptom card with new data
        symptom.symptoms = symptoms

        # Commit changes to the database
        db.session.commit()
        return jsonify({"message": "Symptom card updated successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while updating the symptom card: {str(e)}"}), 500

# Route to delete a symptom card
@medical_journal_bp.route('/delete_symptom/<int:id>', methods=['DELETE'])
def delete_symptom(id):
    try:
        symptom = SymptomCard.query.get(id)

        if not symptom:
            return jsonify({"error": "No symptom card not found"}), 404

        db.session.delete(symptom)
        db.session.commit()
        return jsonify({"message": "Symptom card deleted successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while deleting the symptom card: {str(e)}"}), 500
