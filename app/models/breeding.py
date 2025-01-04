from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base
from app.enums.breeding_status import BREEDING_STATUS


class Breeding(Base):
    __tablename__ = "breeding"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_1_id = Column(UUID(as_uuid=True), nullable=False)
    parent_2_id = Column(UUID(as_uuid=True), nullable=False)
    occurred_at = Column(DateTime(timezone=True), nullable=False, name="occurred_at")
    enclosure_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(Enum(BREEDING_STATUS), nullable=False)
    description = Column(String(1000), nullable=True)

    # Timestamps - keep track of when entry was created and updated
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship to Litter
    litter = relationship("Litter", back_populates="breeding", cascade="all, delete-orphan")

    # Composite unique constraint to avoid duplicate breeding events
    __table_args__ = (
        UniqueConstraint('parent_1_id', 'parent_2_id', 'occurred_at', name='unique_breeding_combination'),
    )

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value

    @validates('parent_1_id', 'parent_2_id')
    def validate_parents(self, key, value):
        # Ensure parents are not the same individual
        if key == 'parent_2_id' and value == self.parent_1_id:
            raise ValueError("Parents must be different individuals.")
        return value

    @validates("occurred_at")
    def validate_occurred_at(self, key, value):
        print(f"Validating occurred_at: {value}, current time: {datetime.now(pytz.UTC)}")
        if value > datetime.now(pytz.UTC):
            raise ValueError("The occurred_at field cannot be set to a future date.")
        return value
