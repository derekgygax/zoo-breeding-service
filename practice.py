from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    create_engine,
    func,
    UniqueConstraint,
    ARRAY,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session, validates
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv
import logging

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load .env variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    logger.error("Database URL is not set. Check your .env file or environment variables.")
    raise ValueError("Database URL is not set. Check your .env file or environment variables.")

# SQLAlchemy setup
logger.debug(f"Setting up database engine with URL: {DATABASE_URL}")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency for creating and closing a database session."""
    db = SessionLocal()
    logger.debug("Database session created.")
    try:
        yield db
    except Exception as e:
        logger.error(f"Error during database session: {e}")
        raise
    finally:
        logger.debug("Closing database session.")
        db.close()

# Enums
class BREEDING_STATUS(str, Enum):
    ATTEMPTED = "ATTEMPTED"
    SUCCESSFUL = "SUCCESSFUL"


class LITTER_RELATION(str, Enum):
    SIBLING = "SIBLING"
    HALF_SIBLING = "HALF_SIBLING"
    PARENT = "PARENT"
    OFFSPRING = "OFFSPRING"


# Models
from sqlalchemy.dialects.postgresql import UUID  # Ensure this import is present
from sqlalchemy import Enum as SQLAlchemyEnum  # Avoid ambiguity with Python Enum

class Breeding(Base):
    __tablename__ = "breeding"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_1_id = Column(UUID(as_uuid=True), nullable=False)
    parent_2_id = Column(UUID(as_uuid=True), nullable=False)
    occurred_at = Column(DateTime(timezone=True), nullable=False)
    enclosure_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(SQLAlchemyEnum(BREEDING_STATUS, name="breeding_status", native_enum=False), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False)

    litter = relationship("Litter", back_populates="breeding", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("parent_1_id", "parent_2_id", "occurred_at", name="unique_breeding_combination"),
    )

    @validates("parent_1_id", "parent_2_id")
    def validate_parents(self, key, value):
        logger.debug(f"Validating {key} with value {value}")
        if key == "parent_2_id" and value == self.parent_1_id:
            logger.error("Parents must be different individuals.")
            raise ValueError("Parents must be different individuals.")
        return value

class Litter(Base):
    __tablename__ = "litter"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    breeding_id = Column(UUID(as_uuid=True), ForeignKey("breeding.id", ondelete="CASCADE"), nullable=False)
    offspring_ids = Column(ARRAY(UUID(as_uuid=True)), nullable=False)
    size = Column(Integer, nullable=False)
    birth_date = Column(DateTime(timezone=True), nullable=False)
    enclosure_id = Column(UUID(as_uuid=True), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False)

    breeding = relationship("Breeding", back_populates="litter")

# Schemas
class BreedingBase(BaseModel):
    parent_1_id: UUID
    parent_2_id: UUID
    occurred_at: datetime
    enclosure_id: UUID
    status: BREEDING_STATUS
    description: Optional[str] = None


class BreedingCreate(BreedingBase):
    pass


class BreedingUpdate(BaseModel):
    status: Optional[BREEDING_STATUS] = None
    description: Optional[str] = None


class BreedingResponse(BreedingBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class LitterBase(BaseModel):
    breeding_id: UUID
    offspring_ids: List[UUID]
    size: int
    birth_date: datetime
    enclosure_id: UUID
    description: Optional[str] = None


class LitterCreate(LitterBase):
    pass


class LitterUpdate(BaseModel):
    description: Optional[str] = None


class LitterResponse(LitterBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# CRUD Services
def create_breeding(db: Session, breeding_data: BreedingCreate) -> Breeding:
    logger.debug(f"Creating a new breeding record: {breeding_data}")
    new_breeding = Breeding(**breeding_data.dict())
    db.add(new_breeding)
    db.commit()
    db.refresh(new_breeding)
    logger.debug(f"Created breeding record: {new_breeding}")
    return new_breeding


def create_litter(db: Session, litter_data: LitterCreate) -> Litter:
    logger.debug(f"Creating a new litter record: {litter_data}")
    new_litter = Litter(**litter_data.dict())
    db.add(new_litter)
    db.commit()
    db.refresh(new_litter)
    logger.debug(f"Created litter record: {new_litter}")
    return new_litter


# Routers
breeding_router = APIRouter(prefix="/breeding", tags=["Breeding"])


@breeding_router.post("/", response_model=BreedingResponse)
def create_breeding_endpoint(breeding_data: BreedingCreate, db: Session = Depends(get_db)):
    logger.info("Handling POST /breeding")
    return create_breeding(db, breeding_data)


litter_router = APIRouter(prefix="/litter", tags=["Litter"])


@litter_router.post("/", response_model=LitterResponse)
def create_litter_endpoint(litter_data: LitterCreate, db: Session = Depends(get_db)):
    logger.info("Handling POST /litter")
    return create_litter(db, litter_data)


# Main App
app = FastAPI()

app.include_router(breeding_router)
app.include_router(litter_router)

@app.on_event("startup")
def on_startup():
    logger.info("Starting up application and creating database tables.")
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    logger.info("Handling GET /")
    return {"message": "Zoo Breeding Service API is running"}
