from uuid import UUID
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import date

class BreedingEventBase(BaseModel):
    parent_1_id: UUID = Field(..., title="Parent 1", description="The id for one of the parents in the breeding event")
    parent_2_id: UUID = Field(..., title="Parent 2", description="The id for one of the parents in the breeding event")
    occurred_at: date = Field(..., title="Date of Breeding", description="The date of the breeding event")
    description: str = Field(..., title="Notes", max_length=1000, description="A description of noteworthy things that happened during the breeding")

    class Config:
        jsonable_encoder = {date: lambda v: v.isoformat()}
        from_attributes = True