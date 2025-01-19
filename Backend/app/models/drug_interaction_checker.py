import requests
import os
from dotenv import load_dotenv

class DrugInteractionChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fda.gov/drug/label.json"

    def check_drug_drug_interaction(self, drug1, drug2):
        # Make API calls for both drugs (you may need to tweak this based on your use case)
        url1 = f"{self.base_url}?search=active_ingredient:{drug1}"
        url2 = f"{self.base_url}?search=active_ingredient:{drug2}"

        try:
            # Call API for drug1
            response1 = requests.get(url1)
            response1.raise_for_status()  # Check if the request was successful
            drug1_data = response1.json()

            # Call API for drug2
            response2 = requests.get(url2)
            response2.raise_for_status()  # Check if the request was successful
            drug2_data = response2.json()

            # Check if the drugs were found in the response
            if not drug1_data['results'] or not drug2_data['results']:
                return {"error": "No information found for one or both drugs."}

            # Here you can handle logic to determine interactions, for now, let's just return the data
            return {
                "drug1_info": drug1_data['results'][0],  # Get the first result (you can add more handling if needed)
                "drug2_info": drug2_data['results'][0]
            }

        except requests.exceptions.RequestException as e:
            return {"error": f"An error occurred while checking the drug interaction: {str(e)}"}
        except ValueError:
            return {"error": "Received invalid JSON response from the API."}

# Example usage
if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("DRUG_API_KEY")  # Assuming your API key is stored in .env file
    checker = DrugInteractionChecker(api_key)

    drug_drug_interaction = checker.check_drug_drug_interaction("aspirin", "ibuprofen")
    print("Drug-Drug Interaction:", drug_drug_interaction)
