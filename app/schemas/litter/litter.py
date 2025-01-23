import datetime
from uuid import UUID

from app.schemas.litter.litter_base import LitterBase

class Litter(LitterBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
