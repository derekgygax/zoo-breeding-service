from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from app.enums.breeding_status import BREEDING_STATUS


# Local Imports, because I'm trying to connect the animals-service database
# I am not sure exactly what needs to be imported here, so I am including everything from enums
from app.enums.breeding_status import BREEDING_STATUS
from app.enums.litter_relation import LITTER_RELATION

class BreedingBase(BaseModel):
    parent_1_id: UUID
    parent_2_id: UUID
    occurred_at: datetime
    enclosure_id: UUID
    status: BREEDING_STATUS
    description: Optional[str] = None


class BreedingCreate(BreedingBase):
    """Schema for creating a new breeding record."""
    pass


class BreedingUpdate(BaseModel):
    """Schema for updating a breeding record."""
    status: Optional[BREEDING_STATUS] = None
    description: Optional[str] = None


class BreedingResponse(BreedingBase):
    """Schema for retrieving a breeding record."""
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
