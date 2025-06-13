from typing import List
from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.submission import SubmissionCreate, SubmissionResponse
from crud.submission import submission
from auth.dependencies import get_current_active_user
from utils.logger import logger

router = APIRouter()


@router.post("/", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
def create_submission(
    submission_in: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a submission for current team"""
    try:
        new_submission = submission.create(db=db, user=current_user, submission_data=submission_in)
        logger.info(f"Submission created by {current_user.email}")
        return new_submission
    except Exception as e:
        logger.error(f"Submission failed: {str(e)}")
        raise


@router.get("/", response_model=List[SubmissionResponse])
def list_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List all submissions of current user's team"""
    return submission.get_team_submissions(db=db, user=current_user)
