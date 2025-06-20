# services/auth_service.py

import jwt
import os
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from revoked_tokens import revoke_token as store_revoked, is_token_revoked

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

def generate_token(user_id, tenant):
    jti = f"{tenant}:{user_id}:{datetime.datetime.utcnow().timestamp()}"
    payload = {
        "sub": str(user_id),
        "tenant": tenant,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        "iat": datetime.datetime.utcnow(),
        "jti": jti
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        jti = decoded.get("jti")
        if is_token_revoked(jti):
            raise InvalidTokenError("Token has been revoked.")
        return decoded
    except ExpiredSignatureError:
        raise InvalidTokenError("Token expired.")
    except Exception as e:
        raise InvalidTokenError(f"Invalid token: {str(e)}")

def revoke(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        jti = decoded.get("jti")
        exp = decoded.get("exp")
        now = datetime.datetime.utcnow().timestamp()
        ttl = int(exp - now)
        store_revoked(jti, ttl)
    except Exception:
        pass
