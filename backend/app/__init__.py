from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update with your database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable modification tracking
    CORS(app)

    db.init_app(app)

    from .routes import auth, cards
    app.register_blueprint(auth.bp)
    app.register_blueprint(cards.bp)

    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from .models import user, card
        db.create_all()  # Create database tables if they don't exist

    return app