from sqlalchemy import Column, String, DateTime, func, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base

#TODO is the relationship for breeding, litter, and offspring right!!
# TODO  create teh animals produced!!!!
#TODO the one-to-one here is probabaly wrong!!!

class Litter(Base):
    __tablename__ = "litter"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    breeding_id = Column(UUID(as_uuid=True),ForeignKey("breeding.id", ondelete="CASCADE"), unique=True)
    size = Column(Integer, nullable=False)
    birth_date = Column(DateTime(timezone=True), nullable=False)
    description = Column(String(1000), nullable=True)

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")


    # Relationship to breeding (one-to-one)
    breeding = relationship("Breeding", back_populates="litter")

    # Relation to animals in the litter, so the offspring (many-to-many)
    # offspring = relationship("Animal", back_populates="litter", cascade="all, delete")


    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value
    
# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone