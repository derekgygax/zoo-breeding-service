from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.litter import Litter
from app.schemas.litter import LitterCreate, LitterUpdate

def create_litter(db: Session, litter_data: LitterCreate) -> Litter:
    new_litter = Litter(**litter_data.dict())
    db.add(new_litter)
    db.commit()
    db.refresh(new_litter)
    return new_litter

def get_litter_by_id(db: Session, litter_id: UUID) -> Litter:
    return db.query(Litter).filter(Litter.id == litter_id).first()

def get_all_litter(db: Session) -> List[Litter]:
    return db.query(Litter).all()

def update_litter(db: Session, litter_id: UUID, litter_data: LitterUpdate) -> Litter:
    litter = db.query(Litter).filter(Litter.id == litter_id).first()
    if not litter:
        return None
    for key, value in litter_data.dict(exclude_unset=True).items():
        setattr(litter, key, value)
    db.commit()
    db.refresh(litter)
    return litter

def delete_litter(db: Session, litter_id: UUID) -> bool:
    litter = db.query(Litter).filter(Litter.id == litter_id).first()
    if not litter:
        return False
    db.delete(litter)
    db.commit()
    return True
