import os
import hashlib
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from typing import Optional

# Read values from Heroku config vars
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "fyvio")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "fyvio")

# Hash the password for verification
ADMIN_PASSWORD_HASH = hashlib.sha256(ADMIN_PASSWORD.encode()).hexdigest()

security = HTTPBearer(auto_error=False)

def verify_password(password: str) -> bool:
    """Verify password against stored hash"""
    return hashlib.sha256(password.encode()).hexdigest() == ADMIN_PASSWORD_HASH

def verify_credentials(username: str, password: str) -> bool:
    """Check if provided username/password match admin credentials"""
    return username == ADMIN_USERNAME and verify_password(password)

def is_authenticated(request: Request) -> bool:
    """Check if user session is authenticated"""
    return request.session.get("authenticated", False)

def require_auth(request: Request):
    """Raise error if not authenticated"""
    if not is_authenticated(request):
        raise HTTPException(status_code=401, detail="Authentication required")
    return True

def get_current_user(request: Request) -> Optional[str]:
    """Return current logged in user from session"""
    if is_authenticated(request):
        return request.session.get("username")
    return None
