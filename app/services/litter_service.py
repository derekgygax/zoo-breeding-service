from sqlalchemy.orm import Session, joinedload
from uuid import UUID
from app.models.litter import Litter as LitterORM
from app.models.breeding_event import BreedingEvent as BreedingEventORM
from app.schemas.litter.litter_full import LitterFull
from fastapi import HTTPException, status

def get_litter_full_by_id(db: Session, litter_id: UUID) -> LitterFull:
    # Query the Litter with the associated BreedingEvent using joinedload
    litter = db.query(LitterORM).options(
        joinedload(LitterORM.breeding_event)
    ).filter(LitterORM.id == litter_id).first()

    if not litter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Litter not found"
        )

    # Validate and convert to LitterFull schema
    return LitterFull.model_validate(litter)
