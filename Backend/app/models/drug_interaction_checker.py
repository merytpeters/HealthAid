"""Drug interaction Checker using Drugbank API"""
import requests
import os
from dotenv import load_dotenv

class DrugInteractionChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fda.gov/drug"

    def check_drug_drug_interaction(self, drug1, drug2):
        url = f"{self.base_url}/drug-interactions"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "drug1": drug1,
            "drug2": drug2
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def check_drug_food_interaction(self, drug, food):
        url = f"{self.base_url}/food-interactions"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "drug": drug,
            "food": food
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

# Example usage
if __name__ == "__main__":
    load_dotenv()
    api_key = os.get("DRUG_API_KEY")
    checker = DrugInteractionChecker(api_key)
    
    drug_drug_interaction = checker.check_drug_drug_interaction("aspirin", "ibuprofen")
    print("Drug-Drug Interaction:", drug_drug_interaction)
    
    drug_food_interaction = checker.check_drug_food_interaction("aspirin", "grapefruit")
    print("Drug-Food Interaction:", drug_food_interaction)
