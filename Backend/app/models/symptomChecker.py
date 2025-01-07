"""Symptom Checker Class using APIMEDIC"""
import requests
import hmac
import hashlib
import base64
import os
from dotenv import load_dotenv

class SymptomChecker:
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
            "Authorization": f"{self.api_key}:{computed_hash_string}"
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
        headers = {
            "Authorization": f"{token}"
        }
        try:
            response = requests.get(url, headers=headers)
            print("Request URL:", url)
            print("Request Headers:", headers)
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.text)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}, Response Content: {response.text}")
            return []

    def get_diagnosis(self, token, symptoms, gender, year_of_birth):
        url = f"{self.base_url}/diagnosis"
        headers = {
            "Authorization": f"{token}"
        }
        params = {
            "symptoms": symptoms,
            "gender": gender,
            "year_of_birth": year_of_birth
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            print("Request URL:", self.auth_url)
            print("Request Headers:", headers)
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.text)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(e)
            return {}


if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("APIMEDIC_API_KEY")
    secret_key = os.getenv("SYMPTOM_CHECKER_SECRET_KEY")
    print("API_KEY:", api_key)
    print("SECRET_KEY:", secret_key)


    if not api_key or not secret_key:
        print("API_KEY or SECRET_KEY environment variable not set")
        exit(1)

    checker = SymptomChecker(api_key, secret_key)
    token = checker.get_token()
    if token:
        print("Token acquired:", token)

        symptoms = checker.get_symptoms(token)
        print("Available symptoms:", symptoms)

        symptoms_list = [10, 15]
        diagnosis = checker.get_diagnosis(token, symptoms_list, "male", 1980)
        print("Diagnosis:", diagnosis)
