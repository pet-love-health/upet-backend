from fastapi import APIRouter, Depends, status
from config.db import get_db

from auth.interfaces.rest.user import endpoint
from fastapi import HTTPException

from petowners.interfaces.rest.resources.petOwner import PetOwnerSchemaGet, PetOwnerSchemaPost, PetOwnerUpdateInformation
from petowners.interfaces.rest.resources.favoriteClinics import FavoriteClinicsGet
from petowners.domain.services.favoriteClinicService import FavoriteClinicService
from veterinaryclinics.interfaces.rest.resources.veterinaryClinic import VeterinaryClinicSchemaGet


from sqlalchemy.orm import Session
from petowners.domain.services.petOwnerService import PetOwnerService

from auth.interfaces.rest.resources.auth import Token
favorite_clinics = APIRouter()
tag = "Favorite Clinics"
endpoint = "/favoriteClinics"

@favorite_clinics.post(endpoint +"/userId/{user_id}/clinicId/{clinic_id}", response_model=bool, status_code=status.HTTP_201_CREATED, tags=[tag])
def toggle_favorite_clinic(user_id: int, clinic_id: int, db: Session = Depends(get_db)):
    return FavoriteClinicService.toggle_favorite_clinic(user_id, clinic_id, db)


@favorite_clinics.get(endpoint+ "/userId/{user_id}", response_model=list[VeterinaryClinicSchemaGet], status_code=status.HTTP_200_OK, tags=[tag])
def get_favorite_clinics(user_id: int, db: Session = Depends(get_db)):
    return FavoriteClinicService.get_favorite_clinics(user_id, db)

