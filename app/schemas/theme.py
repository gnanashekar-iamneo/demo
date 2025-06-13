from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ThemeBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200)
    description: Optional[str] = None

class ThemeCreate(ThemeBase):
    pass

class ThemeUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ThemeResponse(ThemeBase):
    id: int
    is_active: bool
    created_at: datetime
    team_count: Optional[int] = None

    class Config:
        from_attributes = True
