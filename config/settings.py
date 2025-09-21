
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'career-consultant-secret-key-2024'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Session Configuration
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_FILE_THRESHOLD = 500
    
    # Assessment Configuration
    TOTAL_QUESTIONS = 45
    QUESTIONS_PER_CATEGORY = {
        'interests': 12,
        'skills': 10,
        'values': 8,
        'work_style': 8,
        'personality': 7
    }
    
    # Career Matching Configuration
    MATCHING_WEIGHTS = {
        'interests': 0.30,
        'skills': 0.25,
        'values': 0.20,
        'work_style': 0.15,
        'personality': 0.10
    }
    
    # Recommendation Settings
    MAX_RECOMMENDATIONS = 10
    MIN_MATCH_THRESHOLD = 0.60
    
    # Database Configuration (if using database)
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///career_consultant.db'
    
    # API Configuration
    EXTERNAL_API_KEY = os.environ.get('EXTERNAL_API_KEY')
    CACHE_TIMEOUT = 3600  # 1 hour
    
    # UI Configuration
    ITEMS_PER_PAGE = 20
    THEME = 'professional'
    
    # File Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    WTF_CSRF_ENABLED = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
