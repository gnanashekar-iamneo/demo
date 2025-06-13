from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from schemas.auth import Token
from schemas.user import UserCreate, UserResponse, UserLogin
from crud.user import user
from auth.jwt_handler import create_access_token
from exceptions.auth_exceptions import InvalidCredentialsError
from config import settings
from utils.logger import logger

router=APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    try:
        db_user = user.create(db=db, obj_in=user_in)
        logger.info(f"New user registered: {db_user.email}")
        return db_user
    except Exception as e:
        logger.error(f"Registration failed for {user_in.email}: {str(e)}")
        raise


@router.post("/login", response_model=Token)
def login_user(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """Login user and return access token"""
    try:
        db_user = user.authenticate(
            db=db, 
            email=user_credentials.email, 
            password=user_credentials.password
        )
        if not db_user:
            raise InvalidCredentialsError("Invalid email or password")

        access_token_expires = timedelta(minutes=settings.jwt_access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": str(db_user.id), "email": db_user.email},
            expires_delta=access_token_expires
        )
        logger.info(f"User logged in: {db_user.email}")
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error(f"Login failed for {user_credentials.email}: {str(e)}")
        raise


@router.post("/login/form", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Login using OAuth2 form (for OpenAPI docs)"""
    try:
        db_user = user.authenticate(db=db, email=form_data.username, password=form_data.password)
        if not db_user:
            raise InvalidCredentialsError("Invalid username or password")

        access_token_expires = timedelta(minutes=settings.jwt_access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": str(db_user.id), "email": db_user.email},
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error(f"Form login failed for {form_data.username}: {str(e)}")
        raise
router = APIRouter()
