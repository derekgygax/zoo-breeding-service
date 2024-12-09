from sqlalchemy import Column, String, DateTime, func, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base

# TODO Take into account a couple vs the breeding time!! SO NOT THE COMPOSITE CONSTRAINT
#TODO is the relationship for breeding, litter, and offspring right!!
#TODO the one-to-one here is probabaly wrong!!!

class Breeding(Base):
    __tablename__ = "breeding"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_1_id = Column(UUID(as_uuid=True), nullable=False)
    parent_2_id = Column(UUID(as_uuid=True), nullable=False)
    occurred_at = Column(DateTime(timezone=True), nullable=False, name="occurred_at")
    description = Column(String(1000), nullable=True)

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship to Litter
    litter = relationship("Litter", back_populates="breeding", cascade="all, delete-orphan")

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value
    
    # Composite unique constraint
    # TODO Take into account a couple vs the breeding time!! so NOT here
    # __table_args__ = (
    #     UniqueConstraint('parent_1_id', 'parent_2_id', name='unique_breeding_combination'),
    # )

# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone