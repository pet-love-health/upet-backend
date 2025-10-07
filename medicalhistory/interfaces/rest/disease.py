from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db import get_db
from medicalhistory.domain.models.disease import Disease
from medicalhistory.interfaces.rest.resources.disease import DiseaseSchemaGet, DiseaseSchemaPost

diseases = APIRouter()
tag = "Diseases"
endpoint = "/diseases"



