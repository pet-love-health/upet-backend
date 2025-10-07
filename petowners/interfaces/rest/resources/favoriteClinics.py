from datetime import time
from pydantic import BaseModel
from datetime import date
from veterinaryclinics.interfaces.rest.resources.veterinaryClinic import VeterinaryClinicSchemaGet


class FavoriteClinicsGet(BaseModel):
    userId: int
    clinics: list[VeterinaryClinicSchemaGet]

    