from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.theme import Theme
from models.team import Team
from schemas.theme import ThemeCreate, ThemeUpdate
from exceptions.theme_exceptions import ThemeAlreadyExistsError


class CRUDTheme:
    def get_by_title(self, db: Session, *, title: str) -> Optional[Theme]:
        return db.query(Theme).filter(func.lower(Theme.title) == title.lower()).first()

    def create(self, db: Session, *, obj_in: ThemeCreate) -> Theme:
        if self.get_by_title(db, title=obj_in.title):
            raise ThemeAlreadyExistsError(f"Theme '{obj_in.title}' already exists")
        db_obj = Theme(
            title=obj_in.title,
            description=obj_in.description
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_active_themes(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Theme]:
        return db.query(Theme).filter(Theme.is_active == True).offset(skip).limit(limit).all()

    def get_with_team_count(self, db: Session, *, theme_id: int) -> Optional[Theme]:
        theme = db.query(Theme).filter(Theme.id == theme_id).first()
        if theme:
            team_count = db.query(Team).filter(Team.theme_id == theme_id).count()
            setattr(theme, "team_count", team_count)
        return theme

    def deactivate(self, db: Session, *, theme_id: int) -> Optional[Theme]:
        theme = db.query(Theme).filter(Theme.id == theme_id).first()
        if theme:
            theme.is_active = False
            db.add(theme)
            db.commit()
            db.refresh(theme)
        return theme

theme = CRUDTheme()
