from uuid import UUID, uuid4
from datetime import datetime

from pydantic import Field

from app.schemas.breeding_event.breeding_event_base import BreedingEventBase

class BreedingEvent(BreedingEventBase):
    id: UUID = Field(
        ...,
        default_factory=uuid4,
        title="Breeding Record ID",
        description="Unique identifier for this breeding record."
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        title="Created At",
        description="When this record was initially created."
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        title="Updated At",
        description="When this record was last updated."
    )

    class Config:
        from_attributes = True