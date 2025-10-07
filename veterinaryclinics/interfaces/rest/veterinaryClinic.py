from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from appointments.interfaces.rest.resources.availability import AvailabilitySchema
from veterinaryclinics.interfaces.rest.resources.veterinaryClinic import AvailabilitySchemaPost, VeterinaryClinicSchemaGet, VeterinaryClinicSchemaPost
from veterinaryclinics.domain.models.veterinaryClinic import VeterinaryClinic
from veterinaryclinics.domain.services.veterinaryClinicService import VeterinaryClinicService
from config.db import get_db
from fastapi import Depends
from datetime import date, datetime
from veterinarian.interfaces.rest.resources.veterinarian import VeterinarianSchemaGet
veterinary_clinics = APIRouter()
tag = "Veterinary Clinics"
endpoint = "/veterinary_clinics"


@veterinary_clinics.post(endpoint, response_model=VeterinaryClinicSchemaGet, status_code=status.HTTP_201_CREATED, tags=[tag])
def create_veterinary_clinic(clinic: VeterinaryClinicSchemaPost, db: Session = Depends(get_db)):
    return VeterinaryClinicService.create_veterinary_clinic(clinic = clinic, db = db)

@veterinary_clinics.get(endpoint, response_model=list[VeterinaryClinicSchemaGet], status_code=status.HTTP_200_OK, tags=[tag])
def get_veterinary_clinics(db: Session = Depends(get_db)):
    return VeterinaryClinicService.get_veterinary_clinics(db)

@veterinary_clinics.get(endpoint + "/generate_password/{clinic_id}", status_code=status.HTTP_200_OK, tags=[tag])
def generate_unique_password(clinic_id: int, db: Session = Depends(get_db)):
    return VeterinaryClinicService.generate_unique_password(clinic_id, db)

@veterinary_clinics.get(endpoint + "/{clinic_id}", response_model=VeterinaryClinicSchemaGet, status_code=status.HTTP_200_OK, tags=[tag])
def get_veterinary_clinic_by_id(clinic_id: int, db: Session = Depends(get_db)):
    return VeterinaryClinicService.get_veterinary_clinic_by_id(clinic_id, db)

