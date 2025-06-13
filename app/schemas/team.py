from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .user import UserInTeam

class TeamBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=500)

class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    theme_id: Optional[int] = None

class TeamJoin(BaseModel):
    team_id: int

class TeamResponse(TeamBase):
    id: int
    leader_id: int
    theme_id: Optional[int] = None
    created_at: datetime
    members: List[UserInTeam] = []
    member_count: Optional[int] = None

    class Config:
        from_attributes = True
