import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Assuming config.py is in the 'backend' directory.
# If your soccer_cards_app.db is also in 'backend':
db_path = os.path.join(basedir, 'soccer_cards_app.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_should_change_this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key_please_change'
    # Define UPLOAD_FOLDER; adjust 'app/static/uploads' as per your actual structure
    # This assumes UPLOAD_FOLDER is backend/app/static/uploads
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads') 

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'test_jwt_secret_key'
    # This assumes UPLOAD_FOLDER for tests is backend/app/static/uploads_test
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads_test')
    WTF_CSRF_ENABLED = False # Disable CSRF for tests for simplicity