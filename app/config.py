# config.py

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
