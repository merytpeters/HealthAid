from flask import Blueprint, request, jsonify
from app.models.symptomChecker import SymptomChecker
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create a blueprint for symptom checker routes
symptom_checker_bp = Blueprint('symptom_checker', __name__)

# Fetch API keys and secret key from environment variables
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

# Ensure API keys and secret key are available
if not api_key or not secret_key:
    raise ValueError("API_KEY or SECRET_KEY environment variable not set")

# Initialize the SymptomChecker instance
checker = SymptomChecker(api_key, secret_key)

# Route to get a token
@symptom_checker_bp.route('/token', methods=['GET'])
def get_token():
    try:
        token = checker.get_token()
        if token:
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Failed to retrieve token"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get symptoms with the provided token
@symptom_checker_bp.route('/symptoms', methods=['GET'])
def get_symptoms():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Authorization token is missing"}), 400
    
    try:
        symptoms = checker.get_symptoms(token)
        if symptoms:
            return jsonify(symptoms), 200
        else:
            return jsonify({"error": "Failed to retrieve symptoms"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get diagnosis based on symptoms, gender, and year of birth
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
    
    try:
        diagnosis = checker.get_diagnosis(token, symptoms, gender, year_of_birth)
        if diagnosis:
            return jsonify(diagnosis), 200
        else:
            return jsonify({"error": "Failed to retrieve diagnosis"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
