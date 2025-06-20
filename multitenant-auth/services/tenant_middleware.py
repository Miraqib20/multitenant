import os
from functools import wraps
from flask import request, jsonify
import jwt
from dotenv import load_dotenv
from services.db_manager import get_tenant_db

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")

def get_tenant_from_request():
    host = request.host.split(':')[0]  # client1.localhost
    return host.split(".")[0]  # client1

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].replace("Bearer ", "")

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            tenant = get_tenant_from_request()
            db = get_tenant_db(tenant)
            request.user = decoded
            request.db = db
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return f(*args, **kwargs)
    return decorated
