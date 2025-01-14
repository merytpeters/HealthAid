from flask import Blueprint, request, jsonify
from app.models.symptomChecker import SymptomChecker, DiagnosisRecords
from app.models.users import User
import os
from dotenv import load_dotenv
import json
from app.utils.crud import CRUD
from flask_jwt_extended import jwt_required, get_jwt_identity
"""API endpoints
get_possible_diagnosis - POST
"""

# Load environment variables from .env
load_dotenv()

# blueprint for symptom checker routes
symptom_checker_bp = Blueprint('symptom_checker', __name__)

# Fetch API keys and secret key from environment variables
api_key = os.getenv("APIMEDIC_API_KEY")
secret_key = os.getenv("SYMPTOM_CHECKER_SECRET_KEY")

# Ensure API keys and secret key are available
if not api_key or not secret_key:
    raise ValueError("API_KEY or SECRET_KEY environment variable not set")

# Initialize the SymptomChecker instance
checker = SymptomChecker(api_key, secret_key)


@symptom_checker_bp.before_request
@jwt_required()
def protect_symptom_checker_routes():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"error": "User not authenticated"}), 401


@symptom_checker_bp.route('/diagnosis', methods=['POST'])
def get_diagnosis():
    """Query db first 
    if not found then apimedic
    then store to database"""
    try:
        # input to query
        search_terms = request.json.get('search_terms')
        if not search_terms or not isinstance(search_terms, list):
            return jsonify({'error': 'Search terms cannot be empty or invalid'}), 400

        current_user_id = get_jwt_identity()
        user = User.query.filter_by(id=current_user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Retrieve the matched symptoms from the database for the current user
        matched_symptoms_records = DiagnosisRecords.query.filter_by(user_id=current_user_id).all()
        for record in matched_symptoms_records:
            stored_symptoms = record.symptom_names or []
            if set(symptom.lower() for symptom in search_terms) == set(s.lower() for s in stored_symptoms):
                return jsonify({
                    'Possible diagnosis': record.diagnosis,
                    'Probability': f"{record.probability}%"
                }), 200

        # If no matching record found, query APIMEDIC for symptoms and diagnosis
        token = checker.get_token()
        symptoms = checker.get_symptoms(token)
        if symptoms["message"] == "success":
            matching_symptoms_ids = []
            matching_symptoms = []
            for symptom_name in search_terms:
                for symptom in symptoms["data"]:
                    if symptom["Name"].lower() == symptom_name.lower():
                        matching_symptoms_ids.append(symptom.get("ID"))
                        matching_symptoms.append(symptom.get("Name"))
                        break

            if not matching_symptoms_ids:
                return jsonify({'error': 'No matching symptom(s) found'}), 404

        symptoms_list = json.dumps(matching_symptoms_ids)

        # Fetch diagnosis
        diagnosis = checker.get_diagnosis(token, symptoms_list, user.gender, user.date_of_birth.year)
        if diagnosis.get("message") == "success":
            for result in diagnosis["data"]:
                condition = result.get("Issue", {}).get("Name", "Unknown Condition")
                probability = result.get("Issue", {}).get("Accuracy", "N/A")

                # update DiagnosisRecords in database
                new_record = DiagnosisRecords(
                    user_id=current_user_id,
                    symptom_ids=matching_symptoms_ids, 
                    symptom_names=matching_symptoms,
                    diagnosis=condition,
                    probability=probability
                )
                CRUD.create(new_record)

                return jsonify({
                    'Possible diagnosis': condition,
                    'Probability': f"{probability}%"
                }), 200
        return jsonify({'error': 'Diagnosis not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
