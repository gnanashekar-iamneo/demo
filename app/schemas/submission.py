from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SubmissionBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class SubmissionResponse(SubmissionBase):
    id: int
    file_path: str
    file_name: str
    file_size: int
    team_id: int
    created_at: datetime

    class Config:
        from_attributes = True
