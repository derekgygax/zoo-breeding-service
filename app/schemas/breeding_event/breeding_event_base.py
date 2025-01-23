from uuid import UUID
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import date

class BreedingEventBase(BaseModel):
    parent_1_id: UUID = Field(
        ..., 
        title="Parent 1",
        # This while it is a UUID will be a selctor on the front enc
        # So you pick the parent from a drop down
        format="selector",
        description="The id for one of the parents in the breeding event"
    )
    parent_2_id: UUID = Field(
        ..., title="Parent 2", 
        # This while it is a UUID will be a selctor on the front enc
        # So you pick the parent from a drop down
        format="selector",
        description="The id for one of the parents in the breeding event"
    )
    # I decided to make occurred_at just a date
    # So its just a day rather than the time
    occurred_at: date = Field(
        ...,
        title="Breeding Occurred At",
        description="The date of the breeding event",
        examples=["2023-03-01T09:00:00Z"]
    )
    # I feel ya on the Optional but I haven't looked exactly into how
    # handle that on the front end yet. So lets keep everything
    # required at the moment in the schemas
    # description: Optional[str] = Field(
    description: str = Field(
        None,
        title="Breeding Description",
        max_length=1000,
        description="Any details about the breeding event outcome or context."
    )
    description: str = Field(..., title="Notes", max_length=1000, description="A description of noteworthy things that happened during the breeding")

    class Config:
        jsonable_encoder = {date: lambda v: v.isoformat()}
        from_attributes = True