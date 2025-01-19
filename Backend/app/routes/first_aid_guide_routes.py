from flask import Blueprint, request, jsonify
import os
import openai

# Initialize Flask Blueprint
first_aid_bp = Blueprint('first_aid_guide', __name__)

# Set OpenAI API Key from environment variable
openai.api_key = os.getenv('API_KEY')

@first_aid_bp.route('/guide', methods=['POST'])
def first_aid_guide():
    """
    Endpoint for providing first aid guidance using OpenAI's API.
    Accepts a JSON body with a 'query' field specifying the user's query.
    """
    data = request.json
    query = data.get('query', '')

    # Validate input
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        # Use OpenAI's ChatCompletion to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful first aid assistant."},
                {"role": "user", "content": f"Provide first aid guidance for: {query}"}
            ]
        )

        # Extract and return the AI-generated response
        ai_response = response['choices'][0]['message']['content']
        return jsonify({'response': ai_response}), 200

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors gracefully
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500
