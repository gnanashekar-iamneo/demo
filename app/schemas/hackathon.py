from pydantic import BaseModel
from typing import List
from theme import themeResponse

class Create_hackathon(BaseModel):
    id:int
    title:str
    description:str
    theme:List[themeResponse]
    
class HackathonResponse(BaseModel):
    id:int 
    title:str
    description:str
    theme:List[themeResponse]

    class Config:
        orm_mode=True

    