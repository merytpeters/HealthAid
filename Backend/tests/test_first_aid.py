import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from app.routes.first_aid_guide_routes import first_aid_bp  # Adjust import based on your file structure
import json
from unittest.mock import patch


class TestFirstAid(unittest.TestCase):
    def setUp(self):
        """
        This method will be run before each test case.
        It sets up the Flask app and test client.
        """
        self.app = Flask(__name__)
        self.app.register_blueprint(first_aid_bp, url_prefix='/first_aid')
        self.client = self.app.test_client()

    def test_get_first_aid_success(self):
        """
        Test the success case for the /first_aid/guide route.
        """
        with patch('requests.get') as mocked_get:
            # Simulating a successful API response from OpenFDA
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = {
                "results": [{
                    "openfda": {"brand_name": ["Test Product"]},
                    "purpose": ["Pain reliever"],
                    "warnings": ["Warning: Test warning."],
                    "dosage_and_administration": ["Take 1 pill every 8 hours."],
                    "inactive_ingredient": ["Inactive ingredient 1"]
                }]
            }

            response = self.client.post('/first_aid/guide', json={'query': 'headache'})
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertIn("Product Name", data)
            self.assertEqual(data["Product Name"], "Test Product")
            self.assertIn("Purpose", data)
            self.assertIn("Warnings", data)
            self.assertIn("Dosage Information", data)
            self.assertIn("Inactive Ingredients", data)

    def test_get_first_aid_no_query(self):
        """
        Test when no query parameter is provided.
        """
        response = self.client.post('/first_aid/guide', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Query parameter is missing")

    def test_get_first_aid_api_error(self):
        """
        Test when there is an error with the OpenFDA API.
        """
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = Exception("API request failed")

            response = self.client.post('/first_aid/guide', json={'query': 'headache'})
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 500)
            self.assertIn("error", data)
            self.assertEqual(data["error"], "Error fetching data from OpenFDA: API request failed")


if __name__ == '__main__':
    unittest.main()
