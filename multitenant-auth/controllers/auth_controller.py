# controllers/auth_controller.py
from flask import jsonify
from services.db_manager import get_db
from models.user_model import UserModel
from utils.token_utils import create_access_token
from revoked_tokens import revoke_token

def get_tenant_from_request(request):
    host = request.host
    return host.split('.')[0] if '.' in host else "client1"  # fallback for dev

def register_user(request):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    tenant = get_tenant_from_request(request)

    db = get_db(tenant)
    user_model = UserModel(db)
    
    if user_model.create_user(username, password):
        return jsonify({"message": "User registered successfully"}), 200
    else:
        return jsonify({"error": "User already exists"}), 400

def login_user(request):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    tenant = get_tenant_from_request(request)

    db = get_db(tenant)
    user_model = UserModel(db)
    
    user = user_model.get_user(username)
    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token({"sub": username})
    return jsonify({"access_token": token}), 200
