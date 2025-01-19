from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from app.models.drug_interaction_checker import DrugInteractionChecker
import logging

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Load environment variables
load_dotenv()
api_key = os.getenv("DRUG_API_KEY")
checker = DrugInteractionChecker(api_key)

# Create the Blueprint for this module
drug_interaction_checker_bp = Blueprint('drug_interaction_checker', __name__)

@drug_interaction_checker_bp.route('/check_drug_drug_interaction', methods=['GET'])
def check_drug_drug_interaction():
    try:
        drug1 = request.args.get('drug1')
        drug2 = request.args.get('drug2')

        if not drug1 or not drug2:
            logger.warning("Missing parameters: drug1 or drug2 not provided.")
            return jsonify({"error": "Both drug1 and drug2 parameters are required"}), 400

        # Call the checker method
        interaction = checker.check_drug_drug_interaction(drug1, drug2)

        # If there's no result or an error, return the error message
        if "error" in interaction:
            logger.error(f"Error occurred: {interaction['error']}")
            return jsonify(interaction), 500

        # Return the successful interaction result
        return jsonify(interaction)

    except Exception as e:
        logger.exception("Error in check_drug_drug_interaction route.")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@drug_interaction_checker_bp.route('/check_drug_food_interaction', methods=['GET'])
def check_drug_food_interaction():
    try:
        drug = request.args.get('drug')
        food = request.args.get('food')

        if not drug or not food:
            logger.warning("Missing parameters: drug or food not provided.")
            return jsonify({"error": "Both drug and food parameters are required"}), 400

        # Call the checker method
        interaction = checker.check_drug_food_interaction(drug, food)

        # If there's no result or an error, return the error message
        if "error" in interaction:
            logger.error(f"Error occurred: {interaction['error']}")
            return jsonify(interaction), 500

        # Return the successful interaction result
        return jsonify(interaction)

    except Exception as e:
        logger.exception("Error in check_drug_food_interaction route.")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
