from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from app.database import get_db
from app.schemas.breeding import BreedingCreate, BreedingUpdate, BreedingResponse
from app.services.breeding import (
    create_breeding,
    get_breeding_by_id,
    get_all_breeding,
    update_breeding,
    delete_breeding,
)

router = APIRouter(prefix="/breeding", tags=["Breeding"])

# Create a new breeding record
@router.post("/", response_model=BreedingResponse)
def create_breeding_endpoint(breeding_data: BreedingCreate, db: Session = Depends(get_db)):
    return create_breeding(db, breeding_data)

# Get a breeding record by ID
@router.get("/{breeding_id}/", response_model=BreedingResponse)
def get_breeding_endpoint(breeding_id: UUID, db: Session = Depends(get_db)):
    breeding = get_breeding_by_id(db, breeding_id)
    if not breeding:
        raise HTTPException(status_code=404, detail="Breeding record not found")
    return breeding

# Get all breeding records
@router.get("/", response_model=List[BreedingResponse])
def get_all_breeding_endpoint(db: Session = Depends(get_db)):
    return get_all_breeding(db)

# Update a breeding record
@router.put("/{breeding_id}/", response_model=BreedingResponse)
def update_breeding_endpoint(breeding_id: UUID, breeding_data: BreedingUpdate, db: Session = Depends(get_db)):
    updated_breeding = update_breeding(db, breeding_id, breeding_data)
    if not updated_breeding:
        raise HTTPException(status_code=404, detail="Breeding record not found")
    return updated_breeding

# Delete a breeding record
@router.delete("/{breeding_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_breeding_endpoint(breeding_id: UUID, db: Session = Depends(get_db)):
    if not delete_breeding(db, breeding_id):
        raise HTTPException(status_code=404, detail="Breeding record not found")
    return {"detail": "Breeding record deleted successfully"}
