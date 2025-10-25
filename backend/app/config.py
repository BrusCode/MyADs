"""
Application configuration using Pydantic Settings
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import secrets


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    
    # ==============================================
    # Application Settings
    # ==============================================
    APP_NAME: str = "Ads Dashboard Platform"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Analytics platform for Google Ads and Meta Ads"
    ENVIRONMENT: str = "development"
    
    # ==============================================
    # Database Configuration
    # ==============================================
    DATABASE_URL: str
    
    # ==============================================
    # Redis Configuration
    # ==============================================
    REDIS_URL: str
    
    # ==============================================
    # JWT Configuration
    # ==============================================
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # ==============================================
    # Google Ads API
    # ==============================================
    GOOGLE_ADS_DEVELOPER_TOKEN: str = ""
    GOOGLE_ADS_CLIENT_ID: str = ""
    GOOGLE_ADS_CLIENT_SECRET: str = ""
    GOOGLE_ADS_REDIRECT_URI: str = "http://localhost:8000/api/v1/ad-accounts/google-ads/callback"
    
    # ==============================================
    # Meta Ads API
    # ==============================================
    META_APP_ID: str = ""
    META_APP_SECRET: str = ""
    META_REDIRECT_URI: str = "http://localhost:8000/api/v1/ad-accounts/meta-ads/callback"
    
    # ==============================================
    # Email Configuration
    # ==============================================
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@adsdashboard.com"
    SMTP_FROM_NAME: str = "Ads Dashboard Platform"
    
    # ==============================================
    # CORS Configuration
    # ==============================================
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:8080"
    ]
    
    # ==============================================
    # Monitoring
    # ==============================================
    SENTRY_DSN: str = ""
    LOG_LEVEL: str = "INFO"
    
    # ==============================================
    # Pagination
    # ==============================================
    DEFAULT_PAGE_SIZE: int = 50
    MAX_PAGE_SIZE: int = 100
    
    # ==============================================
    # Rate Limiting
    # ==============================================
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # ==============================================
    # Session
    # ==============================================
    SESSION_COOKIE_NAME: str = "ads_dashboard_session"
    SESSION_COOKIE_SECURE: bool = False  # Set to True in production with HTTPS
    
    # ==============================================
    # Celery Configuration
    # ==============================================
    CELERY_BROKER_URL: str = ""
    CELERY_RESULT_BACKEND: str = ""
    
    @property
    def celery_broker(self) -> str:
        """Get Celery broker URL (defaults to REDIS_URL)"""
        return self.CELERY_BROKER_URL or self.REDIS_URL
    
    @property
    def celery_backend(self) -> str:
        """Get Celery result backend URL (defaults to REDIS_URL)"""
        return self.CELERY_RESULT_BACKEND or self.REDIS_URL
    
    # ==============================================
    # Cache Configuration
    # ==============================================
    CACHE_TTL_SECONDS: int = 900  # 15 minutes
    CACHE_METRICS_TTL_SECONDS: int = 300  # 5 minutes
    
    # ==============================================
    # File Upload
    # ==============================================
    MAX_UPLOAD_SIZE_MB: int = 10
    ALLOWED_UPLOAD_EXTENSIONS: List[str] = [".jpg", ".jpeg", ".png", ".pdf", ".xlsx", ".csv"]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


# Create settings instance
settings = Settings()


# ==============================================
# Helper Functions
# ==============================================

def get_database_url() -> str:
    """Get database URL"""
    return settings.DATABASE_URL


def get_redis_url() -> str:
    """Get Redis URL"""
    return settings.REDIS_URL


def is_production() -> bool:
    """Check if running in production"""
    return settings.ENVIRONMENT == "production"


def is_development() -> bool:
    """Check if running in development"""
    return settings.ENVIRONMENT == "development"

