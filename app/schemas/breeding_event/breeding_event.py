from uuid import UUID
from datetime import datetime

from app.schemas.breeding_event.breeding_event_base import BreedingEventBase

class BreedingEvent(BreedingEventBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True