from sqlalchemy import Column, String, DateTime, ForeignKey, ARRAY, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base


class Litter(Base):
    __tablename__ = "litter"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    breeding_id = Column(UUID(as_uuid=True), ForeignKey("breeding.id", ondelete="CASCADE"), nullable=False)  # Link to the breeding event
    offspring_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=False)
    size = Column(Integer, nullable=False)  # Number of offspring in the litter
    birth_date = Column(DateTime(timezone=True), nullable=False)  # Timestamp of birth
    enclosure_id = Column(UUID(as_uuid=True), nullable=False)  # Reference to zoo-enclosures-service
    description = Column(String(1000), nullable=True)  # Optional details about the litter

    # Timestamps - keep track of when entry was created and updated
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship to Breeding (one-to-one)
    breeding = relationship("Breeding", back_populates="litter")

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value

    @validates('size', 'offspring_ids')
    def validate_litter_size(self, key, value):
        # Ensure `size` matches the number of `offspring_ids`
        if key == 'size' and len(self.offspring_ids) != value:
            raise ValueError("Size must match the number of offspring IDs.")
        if key == 'offspring_ids' and len(value) != self.size:
            raise ValueError("The number of offspring IDs must match the size.")
        return value

    @validates('birth_date')
    def validate_birth_date(self, key, value):
        # Ensure `birth_date` is not in the future
        if value > datetime.now(pytz.UTC):
            raise ValueError("The birth_date cannot be set to a future date.")
        return value
