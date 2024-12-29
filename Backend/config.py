#!/usr/bin/env python3
"""Configurations Settings File"""
import os
import openai
from dotenv import load_dotenv


load_dotenv()


class Config:
    """Configuration class"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    API_KEY = os.getenv('API_KEY')
    DRUG_API_KEY = os.getenv('DRUG_API_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # Set up the OpenAI API key

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Flask-Mail Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
