from flask import Blueprint, request, jsonify
import os
import requests

first_aid_bp = Blueprint('first_aid_guide', __name__)

OPENFDA_API_URL = os.getenv('OPENFDA_API_URL', 'https://api.fda.gov/drug/label.json')

def decode_unicode_escape(text):
    if isinstance(text, str):
        # Decode standard unicode escape sequences properly
        text = text.encode('utf-8').decode('unicode_escape')
        # Replace specific Unicode sequences (like \u2022) with corresponding characters
        text = text.replace("\u2022", "•")
        return text
    return text

@first_aid_bp.route('/guide', methods=['POST'])
def first_aid_guide():
    data = request.json
    query = data.get('query', '')

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        # Construct the request URL
        request_url = f"{OPENFDA_API_URL}?search=indications_and_usage:{query}&limit=1"
        print(f"Request URL: {request_url}")  # Debugging: print the request URL

        # Make the API request
        response = requests.get(request_url)
        print(f"Response Status Code: {response.status_code}")  # Debugging: print status code
        print(f"Response Text: {response.text}")  # Debugging: print raw response

        # Check if the response status is okay
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the response
        response_data = response.json()
        print(f"Response Data: {response_data}")  # Debugging: print the response data

        if 'results' in response_data and response_data['results']:
            result = response_data['results'][0]

            # Extract and decode information
            information = {
                'brand_name': decode_unicode_escape(result.get('openfda', {}).get('brand_name', ['N/A'])[0] if 'openfda' in result else 'N/A'),
                'generic_name': decode_unicode_escape(result.get('openfda', {}).get('generic_name', ['N/A'])[0] if 'openfda' in result else 'N/A'),
                'dosage_and_administration': decode_unicode_escape(result.get('dosage_and_administration', 'N/A')),
                'indications_and_usage': decode_unicode_escape(result.get('indications_and_usage', 'N/A')),
                'purpose': decode_unicode_escape(result.get('purpose', 'N/A'))
            }

            return jsonify({'response': information})

        else:
            return jsonify({'error': 'No results found'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
