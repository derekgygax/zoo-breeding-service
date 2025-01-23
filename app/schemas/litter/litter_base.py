from uuid import UUID
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import date

class LitterBase(BaseModel):
    breeding_id: UUID = Field(..., title="Breeding Event", description="The id for the breeding event producing the litter")
    size: int = Field(..., title="Size of the Litter", description="The number of offspring in the litter")
    birth_date: date = Field(..., title="Birth Date", description="Date of birth of the litter")
    description: str = Field(..., title="Notes", max_length=1000, description="Notes about the litter")

    class Config:
        jsonable_encoder = {date: lambda v: v.isoformat()}
        from_attributes = True