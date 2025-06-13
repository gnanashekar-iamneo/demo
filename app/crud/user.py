from typing import Optional, List
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from auth.jwt_handler import get_password_hash, verify_password
from exceptions.user_exceptions import UserAlreadyExistsError


class CRUDUser:
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get(self, db: Session, *, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        if self.get_by_email(db, email=obj_in.email):
            raise UserAlreadyExistsError(f"Email {obj_in.email} exists")
        if self.get_by_username(db, username=obj_in.username):
            raise UserAlreadyExistsError(f"Username {obj_in.username} exists")
        db_obj = User(
            email=obj_in.email,
            username=obj_in.username,
            full_name=obj_in.full_name,
            hashed_password=get_password_hash(obj_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, user: User, obj_in: UserUpdate) -> User:
        if obj_in.full_name is not None:
            user.full_name = obj_in.full_name
        if obj_in.username is not None:
            user.username = obj_in.username
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_password(self, db: Session, *, user: User, new_password: str) -> User:
        user.hashed_password = get_password_hash(new_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if user and verify_password(password, user.hashed_password):
            return user
        return None

    def get_team_members(self, db: Session, *, team_id: int) -> List[User]:
        return db.query(User).filter(User.team_id == team_id).all()

    def get_active_users(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).filter(User.is_active == True).offset(skip).limit(limit).all()

    def delete(self, db: Session, *, user_id: int) -> Optional[User]:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user


user = CRUDUser()
