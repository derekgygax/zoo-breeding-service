import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load the environment variables
load_dotenv()

# Set up logging for database connections and errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DB_URL")
if not DATABASE_URL:
    raise ValueError("Database URL is not set. Check your .env file or environment variables.")

# Set up the SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,             # Maximum number of connections in the pool
    max_overflow=20,          # Extra connections allowed when the pool is full
    pool_timeout=30,          # Timeout for getting a connection from the pool
    pool_recycle=1800         # Recycle connections every 30 minutes
)

# SessionLocal will create a new session when called, tied to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()


def get_db():
    """Dependency for creating and closing a database session."""
    db = SessionLocal()
    try:
        yield db  # Provide the session to the request handler
    except Exception as e:
        logger.error(f"An error occurred with the database session: {e}")
        raise
    finally:
        db.close()  # Close the session after the request


# Optional: Health check function for database connectivity
def check_db_connection():
    """Perform a health check to ensure the database is accessible."""
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        logger.info("Database connection is healthy.")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
