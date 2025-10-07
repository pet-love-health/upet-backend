from fastapi import APIRouter, Depends, status
from config.db import get_db

from auth.interfaces.rest.user import endpoint
from fastapi import HTTPException

from petowners.interfaces.rest.resources.petOwner import PetOwnerSchemaGet, PetOwnerSchemaPost, PetOwnerUpdateInformation
from notifications.interfaces.rest.resources.reminder import ReminderPostSchema, ReminderGetSchema
from notifications.domain.services.reminderService import ReminderService



from sqlalchemy.orm import Session
from petowners.domain.services.petOwnerService import PetOwnerService

from auth.interfaces.rest.resources.auth import Token
reminders = APIRouter()
tag = "Reminders"
endpoint = "/reminders"

@reminders.post(endpoint, response_model=ReminderGetSchema, status_code=status.HTTP_201_CREATED, tags=[tag])
def create_reminder(reminder: ReminderPostSchema, db: Session = Depends(get_db)):
    return ReminderGetSchema.from_orm(ReminderService.create_new_reminder(reminder, db))

@reminders.get(endpoint+ "/userId/{user_id}", response_model=list[ReminderGetSchema], status_code=status.HTTP_200_OK, tags=[tag])
def get_reminders(user_id: int, db: Session = Depends(get_db)):
    return ReminderService.get_reminders(user_id, db)

@reminders.get(endpoint, response_model=list[ReminderGetSchema], status_code=status.HTTP_200_OK, tags=[tag])
def get_all_reminders(db: Session = Depends(get_db)):
    return ReminderService.get_all_reminders(db)
