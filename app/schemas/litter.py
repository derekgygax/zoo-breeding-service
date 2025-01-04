from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

# Local Imports, because I'm trying to connect the animals-service database
# I am not sure exactly what needs to be imported here, so I am including everything from enums
from app.enums.breeding_status import BREEDING_STATUS
from app.enums.litter_relation import LITTER_RELATION

class LitterBase(BaseModel):
    breeding_id: UUID
    offspring_ids: List[UUID]
    size: int
    birth_date: datetime
    enclosure_id: UUID
    description: Optional[str] = None


class LitterCreate(LitterBase):
    """Schema for creating a new litter record."""
    pass


class LitterUpdate(BaseModel):
    """Schema for updating a litter record."""
    description: Optional[str] = None


class LitterResponse(LitterBase):
    """Schema for retrieving a litter record."""
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
