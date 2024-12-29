from flask import Blueprint, request, jsonify
from app.models.symptomChecker import SymptomChecker 
import os
from dotenv import load_dotenv

load_dotenv()

symptom_checker_bp = Blueprint('symptom_checker', __name__)
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

if not api_key or not secret_key:
    raise ValueError("API_KEY or SECRET_KEY environment variable not set")

checker = SymptomChecker(api_key, secret_key)
@symptom_checker_bp.route('/token', methods=['GET'])
def get_token():
    token = checker.get_token()
    if token:
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Failed to retrieve token"}), 500

@symptom_checker_bp.route('/symptoms', methods=['GET'])
def get_symptoms():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Authorization token is missing"}), 400

    symptoms = checker.get_symptoms(token)
    return jsonify(symptoms)

@symptom_checker_bp.route('/diagnosis', methods=['POST'])
def get_diagnosis():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Authorization token is missing"}), 400

    data = request.json
    symptoms = data.get('symptoms')
    gender = data.get('gender')
    year_of_birth = data.get('year_of_birth')

    if not symptoms or not gender or not year_of_birth:
        return jsonify({"error": "Missing required parameters"}), 400

    diagnosis = checker.get_diagnosis(token, symptoms, gender, year_of_birth)
    return jsonify(diagnosis)
