from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.theme import ThemeCreate, ThemeResponse
from crud.theme import theme
from auth.dependencies import get_current_active_user
from utils.logger import logger

router = APIRouter()


@router.post("/", response_model=ThemeResponse, status_code=status.HTTP_201_CREATED)
def create_theme(
    theme_in: ThemeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new theme"""
    try:
        db_theme = theme.create(db=db, obj_in=theme_in)
        logger.info(f"Theme created: {db_theme.title}")
        return db_theme
    except Exception as e:
        logger.error(f"Create theme failed: {str(e)}")
        raise


@router.get("/", response_model=List[ThemeResponse])
def list_themes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List all themes"""
    return theme.get_all(db=db)
