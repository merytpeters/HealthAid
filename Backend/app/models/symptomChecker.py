"""Symptom Checker Class using APIMEDIC"""
import requests
import hmac
import hashlib
import base64
import requests
from app.db import db
from datetime import datetime, timezone

class SymptomChecker:
    """Class to Acces APIMEDIC DATABASE"""
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.auth_url = "https://sandbox-authservice.priaid.ch/login"
        self.base_url = "https://sandbox-healthservice.priaid.ch"

    def get_token(self):
        # Generate HMACMD5 hash
        secret_bytes = self.secret_key.encode('utf-8')
        data_bytes = self.auth_url.encode('utf-8')
        computed_hash = hmac.new(secret_bytes, data_bytes, hashlib.md5).digest()
        computed_hash_string = base64.b64encode(computed_hash).decode('utf-8')

        # Add Authorization header
        headers = {
            "Authorization": f"Bearer {self.api_key}:{computed_hash_string}"
        }

        # Make POST request
        try:
            response = requests.post(self.auth_url, headers=headers)
            response.raise_for_status()
            return response.json().get('Token')
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}, Response Content: {response.text}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_symptoms(self, token):
        url = f"{self.base_url}/symptoms"
        symptoms_url = f'{url}?token={token}&language=en-gb'
        try:
            response = requests.get(symptoms_url)
            response.raise_for_status
            data = response.json()
            return {'message': 'success', 'data': data}
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}, Response Content: {response.text}")
            return []

    def get_diagnosis(self, token, symptoms, gender, year_of_birth):
        url = f"{self.base_url}/diagnosis"
        diagnosis_url = f'{url}?token={token}&symptoms={symptoms}&gender={gender}&year_of_birth={year_of_birth}&language=en-gb'
        try:
            response = requests.get(diagnosis_url)
            response.raise_for_status()
            data = response.json()
            return {'message': 'success', 'data': data}
        except requests.exceptions.HTTPError as e:
            print(e)
            return {}


class DiagnosisRecords(db.Model):
    """Class to Save Frequent Diagnosis (and matched ids from APIMEDIC) for caching"""
    __tablename__ = 'diagnosis_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    symptom_names = db.Column(db.JSON, nullable=False)
    symptom_ids = db.Column(db.JSON, nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    probability = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc))

    user = db.relationship('User', backref=db.backref('diagnosis_records', lazy=True))

    def __init__(self, user_id, symptom_names, symptom_ids, diagnosis, probability):
        self.user_id = user_id
        self.symptom_names = symptom_names
        self.symptom_ids = symptom_ids
        self.diagnosis = diagnosis
        self.probability = probability
        self.count = 1

    def update_count(self):
        self.count += 1
