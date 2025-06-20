from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from config import settings
from schemas.auth import TokenData
from exceptions.auth_exceptions import InvalidTokenError, TokenExpiredError

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.jwt_access_token_expire_minutes)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt


def verify_token(token: str) -> TokenData:
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        user_id: int = payload.get("sub")
        email: str = payload.get("email")
        
        if user_id is None:
            raise InvalidTokenError("Token missing user information")
        
        token_data = TokenData(user_id=user_id, email=email)
        return token_data
    
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError("Token has expired")
    except JWTError:
        raise InvalidTokenError("Could not validate token")
