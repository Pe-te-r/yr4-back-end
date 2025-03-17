import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # App configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret-key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'mburu0116@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-app-password')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'mburu0116@gmail.com')