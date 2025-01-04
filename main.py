from fastapi import FastAPI
from dotenv import load_dotenv

# DB models
from app.routers.breeding import router as breeding_router
from app.routers.litter import router as litter_router

# Other routes from other services possibly?

# Load .env variables in the app
load_dotenv()

app = FastAPI()

# Register the routers
app.include_router(breeding_router)
app.include_router(litter_router)

@app.get("/")
def root():
	return "Welcome to the Zoo Animals Service API"