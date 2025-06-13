from sqlalchemy import Column, Integer, String, Text, Boolean, Index, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    title = Column(String(200), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)

    teams = relationship("Team", back_populates="theme")

    # __table_args__ = (
    #     Index('idx_theme_title_active', 'title', 'is_active'),
    #     Index('idx_theme_active', 'is_active'),
    # )
