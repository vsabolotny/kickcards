from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app.models.user import User
from app.services.auth_service import AuthService

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = AuthService.authenticate_user(email, password)
    
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad email or password"}), 401

@bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    
    if AuthService.register_user(email, password):
        return jsonify({"msg": "User registered successfully"}), 201
    return jsonify({"msg": "User registration failed"}), 400

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="Access granted to protected route")