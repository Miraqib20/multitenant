# revoked_tokens.py
import os
import redis

r = redis.Redis.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379"), 
    decode_responses=True
)

def revoke_token(jti, expires_in):
    """Store JTI in Redis with expiry → revoked."""
    r.setex(f"revoked:{jti}", expires_in, "true")

def is_token_revoked(jti):
    return r.exists(f"revoked:{jti}") == 1
