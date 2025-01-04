from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models here so Alembic can discover them
from .breeding import Breeding
from .litter import Litter

__all__ = ["Base", "Breeding", "Litter"]
