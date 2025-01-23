from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

from app.schemas.litter.litter_full import LitterFull

from app.services import litter_service

router = APIRouter(prefix="/api/v1/litters")

# Get the litter with the breeding event that led to it
@router.get("/{litter_id}/full", tags=["litter"], response_model=LitterFull)
async def get_litter_full_by_id(litter_id: UUID, db: Session = Depends(get_db)):
	return litter_service.get_litter_full_by_id(db=db, litter_id=litter_id)
