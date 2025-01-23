from typing import List, Dict, Any
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

# database
from app.database import get_db

# schemas
from app.schemas.breeding_event.breeding_event import BreedingEvent
from app.schemas.breeding_event.breeding_event_base import BreedingEventBase

# services
from app.services import breeding_events_service


# tags Explanation:
# The tags parameter is used in FastAPI to group endpoints in the automatically generated API documentation (Swagger UI and ReDoc).

router = APIRouter(prefix="/api/v1/breeding-events")

@router.get("/", tags=["breeding_event", "breeding_events"], response_model=List[BreedingEvent])
async def get_breeding_events(db: Session = Depends(get_db)):
	return breeding_events_service.get_all_breeding_events(db=db)


@router.get("/{breeding_event_id}/base", tags=["breeding_event"], response_model=BreedingEventBase)
async def get_breeding_event_base_by_id(breeding_event_id: UUID, db: Session = Depends(get_db)):
	return breeding_events_service.get_breeding_event_base_by_id(db=db, breeding_event_id=breeding_event_id)


@router.post("/", tags=["breeding_event"], status_code=status.HTTP_201_CREATED, response_model=None)
async def add_breeding_event(
	breeding_event_base: BreedingEventBase,
	db: Session = Depends(get_db)
):
	breeding_events_service.add_breeding_event(db=db, breeding_event_base=breeding_event_base)
	return


# # TODO with auth
# # @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED response_model=None, dependencies=[Depends(check_role([ROLE.ADMIN]))])
# @router.post("/", tags=["animal"], status_code=status.HTTP_201_CREATED, response_model=None)
# async def add_animal(
# 	animal: AnimalBase,
# 	# current_user: JWT = Depends(get_current_user),
# 	db: Session = Depends(get_db)
# ):
# 	add_animal_service(db = db, animal = animal)
# 	return

# @router.put("/{animal_id}", tags=["animal"], status_code=status.HTTP_204_NO_CONTENT, response_model=None)
# async def update_animal(
# 	animal_id: UUID,
# 	animal: AnimalBase,
# 	# current_user: JWT = Depends(get_current_user),
# 	db: Session = Depends(get_db)
# ):
# 	update_animal_service(db=db, animal_id=animal_id, animal=animal)
# 	return