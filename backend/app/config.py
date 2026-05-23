import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Government Accident Detection System"
    API_V1_STR: str = ""
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "gov_accident_detection_secure_secret_key_2026_xyz")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Database
    # Default to local SQLite if POSTGRES_URL/DATABASE_URL is not set
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./accident_system.db"
    )
    
    # Twilio (SMS Alerts)
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN", "")
    TWILIO_PHONE_NUMBER: str = os.getenv("TWILIO_PHONE_NUMBER", "")
    
    # Firebase Cloud Messaging
    FIREBASE_CREDENTIALS_PATH: str = os.getenv("FIREBASE_CREDENTIALS_PATH", "")

    # Dev Modes
    VIRTUAL_SMS_LOG_ENABLED: bool = True
    
    class Config:
        case_sensitive = True

settings = Settings()
