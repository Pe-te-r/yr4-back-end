import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # App secret key
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "superjwtsecret")  # JWT key
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")  # SQLite .db file
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking (performance boost)

