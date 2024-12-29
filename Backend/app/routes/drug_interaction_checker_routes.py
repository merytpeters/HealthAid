from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from app.models.drug_interaction_checker import DrugInteractionChecker

load_dotenv()
api_key = os.getenv("DRUG_API_KEY")
checker = DrugInteractionChecker(api_key)

drug_interaction_checker_bp = Blueprint('drug_interaction_checker', __name__)

@drug_interaction_checker_bp.route('/check_drug_drug_interaction', methods=['GET'])
def check_drug_drug_interaction():
    drug1 = request.args.get('drug1')
    drug2 = request.args.get('drug2')
    if not drug1 or not drug2:
        return jsonify({"error": "Both drug1 and drug2 parameters are required"}), 400
    interaction = checker.check_drug_drug_interaction(drug1, drug2)
    return jsonify(interaction)

@drug_interaction_checker_bp.route('/check_drug_food_interaction', methods=['GET'])
def check_drug_food_interaction():
    drug = request.args.get('drug')
    food = request.args.get('food')
    if not drug or not food:
        return jsonify({"error": "Both drug and food parameters are required"}), 400
    interaction = checker.check_drug_food_interaction(drug, food)
    return jsonify(interaction)
