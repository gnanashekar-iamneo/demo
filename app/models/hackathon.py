from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Hackathon(Base):
    __tablename__ = "hackathons"  # Purpose: Tells SQLAlchemy what name to give this table in the DB.
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the hackathon table
    title = Column(String(50), unique=True, index=True, nullable=False)  # Unique name for the hackathon
    description = Column(String(500), nullable=True)  # Description of the hackathon

    themes = relationship("Theme", back_populates="hackathon")  # Relationship to the theme table

    