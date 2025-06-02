from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

class AuthService:
    @staticmethod
    def register_user(email, password):
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)