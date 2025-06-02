from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  # Define the SQLAlchemy instance globally
print(f"ID of db in app/__init__.py (after definition): {id(db)}") # DIAGNOSTIC

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    backend_dir = os.path.dirname(basedir)
    db_path = os.path.join(backend_dir, 'soccer_cards_app.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)
    print(f"ID of db in app/__init__.py (after init_app): {id(db)}") # DIAGNOSTIC
    print(f"App instance for init_app: {id(app)}") # DIAGNOSTIC

    from .routes import auth as auth_blueprint
    from .routes import cards as cards_blueprint
    app.register_blueprint(auth_blueprint.bp)
    app.register_blueprint(cards_blueprint.bp)

    with app.app_context():
        from . import models
        db.create_all()

    return app