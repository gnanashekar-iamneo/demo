from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.team import TeamCreate, TeamResponse, TeamUpdate, TeamJoin
from crud.team import team
from crud.user import user as user_crud
from auth.dependencies import get_current_active_user
from exceptions.team_exceptions import TeamNotFoundError, NotTeamLeaderError, CannotLeaveAsLeaderError
from exceptions.user_exceptions import UserNotFoundError
from utils.logger import logger

router = APIRouter()


@router.post("/", response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
def create_team(
    team_in: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new team (user becomes leader)"""
    try:
        db_team = team.create(db=db, obj_in=team_in, leader=current_user)
        logger.info(f"Team created: {db_team.name} by {current_user.email}")
        return db_team
    except Exception as e:
        logger.error(f"Team creation failed: {str(e)}")
        raise


@router.get("/my-team", response_model=TeamResponse)
def get_my_team(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get current user's team"""
    if not current_user.team_id:
        raise UserNotFoundError("You are not in any team")

    db_team = team.get(db=db, id=current_user.team_id)
    if not db_team:
        raise TeamNotFoundError("Team not found")

    return db_team


@router.post("/join", response_model=TeamResponse)
def join_team(
    team_join: TeamJoin,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Join an existing team"""
    try:
        db_team = team.get(db=db, id=team_join.team_id)
        if not db_team:
            raise TeamNotFoundError("Team not found")

        updated_team = team.add_member(db=db, team=db_team, user=current_user)
        logger.info(f"User {current_user.email} joined team {db_team.name}")
        return updated_team
    except Exception as e:
        logger.error(f"Team join failed: {str(e)}")
        raise


@router.post("/leave")
def leave_team(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Leave current team"""
    try:
        if not current_user.team_id:
            raise UserNotFoundError("You are not in any team")

        db_team = team.get(db=db, id=current_user.team_id)
        if not db_team:
            raise TeamNotFoundError("Team not found")

        if current_user.id == db_team.leader_id:
            raise CannotLeaveAsLeaderError()

        team.remove_member(db=db, team=db_team, user=current_user)
        logger.info(f"User {current_user.email} left team {db_team.name}")
        return {"message": "Successfully left the team"}
    except Exception as e:
        logger.error(f"Leave team failed: {str(e)}")
        raise


@router.put("/theme/{theme_id}", response_model=TeamResponse)
def select_team_theme(
    theme_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Select a theme for the team (only leader can choose)"""
    try:
        if not current_user.team_id:
            raise UserNotFoundError("You are not in any team")

        db_team = team.get(db=db, id=current_user.team_id)
        if not db_team:
            raise TeamNotFoundError("Team not found")

        if db_team.leader_id != current_user.id:
            raise NotTeamLeaderError("Only team leader can choose theme")

        updated_team = team.set_theme(db=db, team=db_team, theme_id=theme_id)
        logger.info(f"Theme selected for team {db_team.name} by {current_user.email}")
        return updated_team
    except Exception as e:
        logger.error(f"Select theme failed: {str(e)}")
        raise
