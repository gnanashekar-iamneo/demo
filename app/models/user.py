import uuid
from sqlalchemy import UUID, Column, DateTime, Index, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users" #Purpose: Tells SQLAlchemy what name to give this table in the DB.
    id=Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
        )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
   
    full_name = Column(String(255), nullable=False)
    username = Column(String(50), unique=True, index=True,nullable=False)  # Unique username for the user
    email = Column(String(100), unique=True, index=True,nullable=False)  # Unique enumerated ID for the user
    hasded_password = Column(String(512), nullable=False)  # Flag to check if the user has set a password

    is_team_leader = Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    
    teamid=Column(Integer,ForeignKey("teams.id"),nullable=True)  # Foreign key to the team table

    led_team = relationship("Team", back_populates="leader", foreign_keys="Team.leader_id")
    team=relationship("Team", back_populates="members")  # Relationship to the team table

    # __table_args__ = (
    #     Index('idx_user_email_active', 'email', 'is_active'),
    #     Index('idx_user_team_leader', 'team_id', 'is_team_leader'),
    # )
        