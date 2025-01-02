import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Configuration class"""

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret Key for Flask
    SECRET_KEY = os.getenv('SECRET_KEY')  
    
    # API Key for OpenAI
    API_KEY = os.getenv('API_KEY')

    DRUG_API_KEY = os.getenv('DRUG_API_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    # JWT Secret Key
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Flask-Mail Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # openFDA API URL
    OPENFDA_API_URL = os.getenv('OPENFDA_API_URL')
