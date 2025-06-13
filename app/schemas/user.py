from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# base model to reduce dry coide 
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)

# payload when creating a new user
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)

# payload when updating user profile
class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    password: Optional[str] = Field(None, min_length=6, max_length=100)

# When logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# For API responses
class UserResponse(UserBase):
    id: int
    is_active: bool
    is_team_leader: bool
    team_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Used inside team responses to show user info
class UserInTeam(BaseModel):
    id: int
    username: str
    full_name: str
    is_team_leader: bool

    class Config:
        from_attributes = True
