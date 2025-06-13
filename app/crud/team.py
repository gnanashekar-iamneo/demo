from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.team import Team
from models.user import User
from schemas.team import TeamCreate, TeamUpdate
from exceptions.team_exceptions import (
    TeamAlreadyExistsError, TeamNotFoundError, TeamFullError,
    UserAlreadyTeamLeaderError, TeamAlreadyHasThemeError
)
from exceptions.user_exceptions import UserAlreadyInTeamError


class CRUDTeam:
    def get_by_name(self, db: Session, *, name: str) -> Optional[Team]:
        return db.query(Team).filter(func.lower(Team.name) == name.lower()).first()

    def create(self, db: Session, *, obj_in: TeamCreate, leader: User) -> Team:
        if self.get_by_name(db, name=obj_in.name):
            raise TeamAlreadyExistsError(f"Team '{obj_in.name}' already exists")
        if leader.is_team_leader:
            raise UserAlreadyTeamLeaderError("User is already a team leader")
        if leader.team_id:
            raise UserAlreadyInTeamError("User is already in a team")

        db_obj = Team(
            name=obj_in.name,
            description=obj_in.description,
            leader_id=leader.id
        )
        db.add(db_obj)
        db.flush()
        leader.is_team_leader = True
        leader.team_id = db_obj.id
        db.add(leader)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_member(self, db: Session, *, team: Team, user: User) -> Team:
        if user.team_id:
            raise UserAlreadyInTeamError("User already in a team")
        member_count = db.query(User).filter(User.team_id == team.id).count()
        if member_count >= 4:
            raise TeamFullError("Team is full")
        user.team_id = team.id
        db.add(user)
        db.commit()
        db.refresh(team)
        return team

    def remove_member(self, db: Session, *, team: Team, user: User) -> Team:
        if user.id == team.leader_id:
            raise Exception("Leader cannot leave the team")
        user.team_id = None
        db.add(user)
        db.commit()
        db.refresh(team)
        return team

    def select_theme(self, db: Session, *, team: Team, theme_id: int) -> Team:
        if team.theme_id:
            raise TeamAlreadyHasThemeError("Theme already selected")
        team.theme_id = theme_id
        db.add(team)
        db.commit()
        db.refresh(team)
        return team

    def get_with_members(self, db: Session, *, team_id: int) -> Optional[Team]:
        return db.query(Team).filter(Team.id == team_id).first()

    def get_user_team(self, db: Session, *, user_id: int) -> Optional[Team]:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.team_id:
            return db.query(Team).filter(Team.id == user.team_id).first()
        return None

    def delete_team(self, db: Session, *, team: Team) -> bool:
        db.query(User).filter(User.team_id == team.id).update({
            "team_id": None,
            "is_team_leader": False
        })
        db.delete(team)
        db.commit()
        return True

team = CRUDTeam()
