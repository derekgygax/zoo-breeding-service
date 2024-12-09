from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
from app.models.breeding import Breeding
from app.models.litter import Litter

# Other routes
# from app.routers.animals import router as animals_router

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the other routers
# app.include_router(animals_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Animals Service API"