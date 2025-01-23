from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field

from app.schemas.litter.litter_base import LitterBase

class Litter(LitterBase):
    id: UUID = Field(
        default_factory=uuid4,
        title="Litter ID",
        description="Unique identifier for this litter."
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        title="Created At",
        description="When this litter record was created."
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        title="Updated At",
        description="When this litter record was last updated."
    )
