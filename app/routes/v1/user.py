from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserResponse, UserUpdate
from crud.user import user
from auth.dependencies import get_current_active_user
from utils.logger import logger

router = APIRouter()


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Get current user information"""
    return current_user


@router.put("/me", response_model=UserResponse)
def update_current_user(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update current user information"""
    try:
        if user_update.password:
            current_user = user.update_password(
                db=db, 
                user=current_user, 
                new_password=user_update.password
            )
            user_update.password = None
        
        updated_user = user.update(db=db, db_obj=current_user, obj_in=user_update)
        logger.info(f"User updated: {updated_user.email}")
        return updated_user
    except Exception as e:
        logger.error(f"User update failed for {current_user.email}: {str(e)}")
        raise


@router.get("/", response_model=List[UserResponse])
def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get list of users (active only)"""
    return user.get_active_users(db=db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get user by ID"""
    db_user = user.get(db=db, id=user_id)
    if not db_user:
        from exceptions.user_exceptions import UserNotFoundError
        raise UserNotFoundError("User not found")
    return db_user
