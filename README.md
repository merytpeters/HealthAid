# HealthAid
HealthAid is a comprehensive personal health management app designed to address common medical needs. This project serves as a final portfolio submission for the Software Engineering program at ALX. The app incorporates essential health management features such as a drug interaction checker, a symptom checker, pill reminders, a first aid guide, a health symptoms journal, and a home medicine inventory.

It aims to empower users to manage their health proactively and safely by providing easy-to-use tools. The app is designed to help users track symptoms, ensure safe medication use, and respond to medical emergencies efficiently.
## Features
### 1. Drug Interaction Checker
- Helps users check the interactions between different medications, ensuring they take them safely.

### 2. Symptom Checker
- Allows users to input symptoms and get preliminary health insights to help them understand potential health conditions.

### 3. Pill Reminders
- Users can set reminders to take their medication on time, with notifications to ensure adherence to prescribed schedules.

### 4. First Aid Guide
- Provides quick access to essential first aid information for various medical emergencies, helping users respond appropriately when necessary.

### 5. Health Symptoms Journal
- Enables users to log their symptoms and track their health over time, giving them insights into their wellness.

### 6. Home Medicine Inventory
- Organizes and tracks medications at home, allowing users to manage their medication stock and avoid running out of essential drugs.

## Technologies Used
HealthAid is built with the following technologies:

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Notifications**: Flask-Mail for sending pill reminders
- **APIs**: Custom APIs for the Drug Interaction Checker and Symptom Checker

## Setup and Installation
To run HealthAid locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/merytpeters/HealthAid.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Create a `.env` file in the root directory and add the necessary variables (e.g., database configurations, API keys).

4. Run the application:
   ```bash
   python app.py
   ```

The app will be accessible on your local machine at `http://localhost:5000`.

## Authors
HealthAid was developed by the following individuals:

- **Afuah Sekyiwaa Adusei** - Frontend Developer and Project Manager
   GitHub: [Afuah-Sekyiwaa-Adusei](https://github.com/)
   Email: 

- **Precious Appiah** - Frontend Developer
   GitHub: [Precious Appiah](https://github.com/)
   Email:

- **Akpevweoghene Edafe** - Backend Developer and Project Manager
   GitHub: [Akpevweoghene Edafe](https://github.com/)
   Email: 

- **Isah Abdulsalam** - Backend Developer
   GitHub: [Isah Abdulsalam](https://github.com/Isah Abdulsalam)
   Email: [Isah Abdulsalam] (isahabdulsalam416@gmail.com)
  
## Acknowledgements
We would like to express our sincere gratitude to the ALX Software Engineering program for providing the tools and resources that allowed us to develop this project. We also appreciate the support and feedback from our peers, mentors, and anyone who has contributed their expertise.

This project aims to provide useful tools for personal health management, but it is important to note that HealthAid does not replace medical consultations with professionals. The information provided in the app is based on general guidelines and may not always be 100% accurate. Always consult with a physician for a proper diagnosis.

## Challenges
This project came with several challenges:

1. **Regulatory Requirements**: Health apps are typically regulated by health organizations, but due to time constraints, we were unable to ensure full compliance with all regulatory standards.

2. **Accuracy of Information**: While we strived to provide reliable data, the app cannot guarantee 100% accuracy in diagnoses or medication interactions.

3. **API Integration**: Integrating APIs for the Symptom Checker and Drug Interaction Checker posed technical difficulties, especially with ensuring the accuracy and reliability of the data provided.

4. **Time Constraints**: Due to the strict timeline for the final portfolio submission, we were unable to implement some additional features and complete all documentation.

## Conclusion
HealthAid is designed to serve as a reliable health management assistant, empowering users to take control of their wellness. While it provides valuable features such as medication tracking, symptom logging, and first aid information, it is not intended to replace professional healthcare services. We are proud of the work completed during this project and look forward to future updates that will further enhance its capabilities.
