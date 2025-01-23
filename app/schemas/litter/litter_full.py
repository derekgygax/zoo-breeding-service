

from pydantic import Field
from app.schemas.breeding_event.breeding_event import BreedingEvent
from app.schemas.litter.litter import Litter


class LitterFull(Litter):
    breeding_event: BreedingEvent = Field(
        ...,
        title="Breeding Event",
        description="The breeding event to produce the litter"
    )