from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(500), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_size = Column(Integer, nullable=False)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)

    team = relationship("Team", back_populates="submissions")

    # __table_args__ = (
    #     Index('idx_submission_team_created', 'team_id', 'created_at'),
    #     Index('idx_submission_title', 'title'),
    # )
