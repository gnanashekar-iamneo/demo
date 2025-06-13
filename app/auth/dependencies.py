from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from .jwt_handler import verify_token
from exceptions.auth_exceptions import InvalidTokenError, AuthenticationError
from exceptions.user_exceptions import UserNotFoundError, UserInactiveError

# Security scheme
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    try:
        token_data = verify_token(credentials.credentials)
        user = db.query(User).filter(User.id == token_data.user_id).first()
        
        if user is None:
            raise UserNotFoundError("User not found")
        
        if not user.is_active:
            raise UserInactiveError("User account is inactive")
        
        return user
    
    except (InvalidTokenError, UserNotFoundError, UserInactiveError):
        raise
    except Exception:
        raise AuthenticationError("Could not validate credentials")


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current active user (alias for clarity)"""
    return current_user


def get_team_leader(current_user: User = Depends(get_current_user)) -> User:
    """Ensure current user is a team leader"""
    if not current_user.is_team_leader:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only team leaders can perform this action"
        )
    return current_user
