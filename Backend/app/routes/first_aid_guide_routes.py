from flask import Blueprint, request, jsonify
import openai
from app.utils.crud import CRUD

# Blueprint for first aid guide routes
first_aid_bp = Blueprint('first_aid', __name__)

# Route to handle first aid guide queries
@first_aid_bp.route('/guide', methods=['POST'])
def get_first_aid():
    query = request.json.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Call the function that interacts with OpenAI API
    result = CRUD.get_first_aid_guide(query)

    if result:
        return jsonify({"first_aid_info": result}), 200
    else:
        return jsonify({"error": "Unable to fetch first aid information"}), 500
