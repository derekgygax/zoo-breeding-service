from sqlalchemy.orm import load_only
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# models
from app.models.breeding_event import BreedingEvent as BreedingEventORM

# schemas
from app.schemas.breeding_event.breeding_event import BreedingEvent as BreedingEventSchema
from app.schemas.breeding_event.breeding_event_base import BreedingEventBase


# TODO CAREFULE WITH THIS ONE!!!
# I do NOT know if you can go from the model to the schema like that
# or if you need a converter!!
def get_all_breeding_events(db: Session) -> List[BreedingEventSchema]:
    return db.query(BreedingEventORM).all()

def get_breeding_event_base_by_id(db: Session, breeding_event_id: UUID) -> BreedingEventBase:
    breeding_event = db.query(BreedingEventORM).filter(BreedingEventORM.id == breeding_event_id).options(
        load_only(
            BreedingEventORM.parent_1_id,
            BreedingEventORM.parent_2_id,
            BreedingEventORM.occurred_at,
            BreedingEventORM.description
        )
    ).first()
    
    if not breeding_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Breeding Event not found"
        )
    
    return BreedingEventBase.model_validate(breeding_event)

def add_breeding_event(db: Session, breeding_event_base: BreedingEventBase) -> None:
    # The parent validation would have to go to animals-service
    # so that part still needs to be figured out
    
    db_breeding_event = BreedingEventORM(**breeding_event_base.model_dump())
    # Print the stuff in db_post
    # print(vars(db_animal))
    db.add(db_breeding_event)
    db.commit()
    db.refresh(db_breeding_event)
    return