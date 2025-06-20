# routes/auth_routes.py
from flask import Blueprint, request, jsonify
from controllers.auth_controller import register_user, login_user
from utils.token_utils import verify_token

bp = Blueprint("auth", __name__, url_prefix="/api")

@bp.route("/register", methods=["POST"])
def register():
    return register_user(request)

@bp.route("/login", methods=["POST"])
def login():
    return login_user(request)

@bp.route("/dashboard", methods=["GET"])
def dashboard():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    token = auth.split(" ")[1]
    try:
        payload = verify_token(token)
        username = payload.get("sub")
        return jsonify({"message": f"Hello, {username}! This is your dashboard."})
    except Exception:
        return jsonify({"error": "Invalid or expired token"}), 401
@bp.route("/whoami", methods=["GET"])
def whoami():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    token = auth.split(" ")[1]
    try:
        payload = verify_token(token)
        username = payload.get("sub")
        tenant = request.host.split('.')[0] if '.' in request.host else "client1"
        return jsonify({
            "username": username,
            "tenant": tenant
        })
    except Exception:
        return jsonify({"error": "Invalid or expired token"}), 401
