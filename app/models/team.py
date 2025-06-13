from sqlalchemy import Column, Integer, String, ForeignKey, Index, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(500), nullable=True)

    leader_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=True, index=True)

    leader = relationship("User", back_populates="led_team", foreign_keys=[leader_id])
    members = relationship("User", back_populates="team", foreign_keys="User.team_id")
    theme = relationship("Theme", back_populates="teams")
    submissions = relationship("Submission", back_populates="team")

    # __table_args__ = (
    #     Index('idx_team_leader_theme', 'leader_id', 'theme_id'),
    #     Index('idx_team_name_lower', 'lower(name)'),
    #     CheckConstraint('leader_id IS NOT NULL', name='team_must_have_leader'),
    # )
