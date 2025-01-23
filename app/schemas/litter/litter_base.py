from uuid import UUID
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import date

class LitterBase(BaseModel):
    breeding_id: UUID = Field(
        ..., 
        title="Breeding Event", 
        description="Breeding event from which this litter resulted."
    )
    size: int = Field(
        ...,
        title="Number of Offspring",
        description="How many offspring were in this litter."
    )
    birth_date: date= Field(
        ...,
        title="Birth Date",
        description="When the litter was born."
    )
    # description: Optional[str] = Field(
    description: str = Field(
        ...,
        title="Litter Description",
        max_digits=1000,
        description="Additional notes about this litter's characteristics or status."
    )

    class Config:
        jsonable_encoder = {date: lambda v: v.isoformat()}
        from_attributes = True