from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from app.database import get_db
from app.schemas.litter import LitterCreate, LitterUpdate, LitterResponse
from app.services.litter import (
    create_litter,
    get_litter_by_id,
    get_all_litter,
    update_litter,
    delete_litter,
)

router = APIRouter(prefix="/litter", tags=["Litter"])

# Create a new litter record
@router.post("/", response_model=LitterResponse)
def create_litter_endpoint(litter_data: LitterCreate, db: Session = Depends(get_db)):
    return create_litter(db, litter_data)

# Get a litter record by ID
@router.get("/{litter_id}/", response_model=LitterResponse)
def get_litter_endpoint(litter_id: UUID, db: Session = Depends(get_db)):
    litter = get_litter_by_id(db, litter_id)
    if not litter:
        raise HTTPException(status_code=404, detail="Litter record not found")
    return litter

# Get all litter records
@router.get("/", response_model=List[LitterResponse])
def get_all_litter_endpoint(db: Session = Depends(get_db)):
    return get_all_litter(db)

# Update a litter record
@router.put("/{litter_id}/", response_model=LitterResponse)
def update_litter_endpoint(litter_id: UUID, litter_data: LitterUpdate, db: Session = Depends(get_db)):
    updated_litter = update_litter(db, litter_id, litter_data)
    if not updated_litter:
        raise HTTPException(status_code=404, detail="Litter record not found")
    return updated_litter

# Delete a litter record
@router.delete("/{litter_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_litter_endpoint(litter_id: UUID, db: Session = Depends(get_db)):
    if not delete_litter(db, litter_id):
        raise HTTPException(status_code=404, detail="Litter record not found")
    return {"detail": "Litter record deleted successfully"}
