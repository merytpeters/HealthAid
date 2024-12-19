import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:////data/data/com.termux/files/home/HealthAid/Backend/instance/health_aid.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'd47e5065b74185b9cac9bb76ab40adf75639034a146f0f1eb01a27ba5b6419b0')
