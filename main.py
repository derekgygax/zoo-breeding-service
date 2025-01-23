from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
from app.models.breeding_event import BreedingEvent
from app.models.litter import Litter

# Other routes
from app.routers.breeding_events import router as breeding_events_router

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the other routers
app.include_router(breeding_events_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Animals Service API"