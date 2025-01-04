from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.breeding import Breeding
from app.schemas.breeding import BreedingCreate, BreedingUpdate

def create_breeding(db: Session, breeding_data: BreedingCreate) -> Breeding:
    new_breeding = Breeding(**breeding_data.dict())
    db.add(new_breeding)
    db.commit()
    db.refresh(new_breeding)
    return new_breeding

def get_breeding_by_id(db: Session, breeding_id: UUID) -> Breeding:
    return db.query(Breeding).filter(Breeding.id == breeding_id).first()

def get_all_breeding(db: Session) -> List[Breeding]:
    return db.query(Breeding).all()

def update_breeding(db: Session, breeding_id: UUID, breeding_data: BreedingUpdate) -> Breeding:
    breeding = db.query(Breeding).filter(Breeding.id == breeding_id).first()
    if not breeding:
        return None
    for key, value in breeding_data.dict(exclude_unset=True).items():
        setattr(breeding, key, value)
    db.commit()
    db.refresh(breeding)
    return breeding

def delete_breeding(db: Session, breeding_id: UUID) -> bool:
    breeding = db.query(Breeding).filter(Breeding.id == breeding_id).first()
    if not breeding:
        return False
    db.delete(breeding)
    db.commit()
    return True
