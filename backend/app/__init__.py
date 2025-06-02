from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager  # Import JWTManager
import os
from config import Config, TestingConfig # Make sure to import your configs

db = SQLAlchemy()  # Define the SQLAlchemy instance globally
jwt = JWTManager()  # Create an instance of JWTManager
print(f"ID of db in app/__init__.py (after definition): {id(db)}")  # DIAGNOSTIC

def create_app(config_name='default'):
    app = Flask(__name__)

    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config) # Default config

    # --- Configure JWT ---
    # It's crucial to set a secret key for JWT.
    # This key is used to sign the JWTs. Keep it secret in production!
    # You can generate a good secret key using:
    # python -c 'import secrets; print(secrets.token_hex(32))'
    # app.config["JWT_SECRET_KEY"] = "e1d3875de77feccd01d161ff2359bae9d5cce6d6edc30d72e5d57160ba220d9f"  # CHANGE THIS!
    # You can also configure token locations, expiration times, etc.
    # app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # basedir = os.path.abspath(os.path.dirname(__file__))
    # backend_dir = os.path.dirname(basedir)
    # db_path = os.path.join(backend_dir, 'soccer_cards_app.db')

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)  # Initialize JWTManager with the app
    print(f"ID of db in app/__init__.py (after init_app): {id(db)}")  # DIAGNOSTIC
    print(f"App instance for init_app: {id(app)}")  # DIAGNOSTIC

    from .routes import auth as auth_blueprint
    from .routes import cards as cards_blueprint
    app.register_blueprint(auth_blueprint.bp, url_prefix='/auth')
    app.register_blueprint(cards_blueprint.bp, url_prefix='/api')

    # Ensure db.create_all() is called only when not testing or with appropriate context
    if config_name != 'testing':
        with app.app_context():
            from . import models
            db.create_all()

    return app