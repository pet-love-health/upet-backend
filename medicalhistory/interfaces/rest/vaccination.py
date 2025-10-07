from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db import get_db
from medicalhistory.domain.models.vaccine  import Vaccine as Vaccination
from medicalhistory.interfaces.rest.resources.vaccination import VaccinationSchemaGet, VaccinationSchemaPost

vaccinations = APIRouter()
tag = "Vaccinations"
endpoint = "/vaccinations"

