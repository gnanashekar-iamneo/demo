from sqlalchemy.orm import Session
from models.hackathon import Hackathon
from schemas.hackathon import Create_hackathon
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


def create_hackathon(db:Session,hack:Create_hackathon):
    db_hack=Hackathon(
        id=hack.id,
        title=hack.title,

    )
    try:
        db.add(db_hack)
        db.commit()
        db.refresh(db_hack)
        return db_hack
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="hackathon already exists"
        )

def get_hackathon_by_id(db:Session,id:str):
    return db.query(Hackathon).filter(Hackathon.id==id).first()

