import random
import string
import datetime
from sqlalchemy.orm import Session
from veterinaryclinics.domain.models.otps import OTP
from config.db import get_db
from fastapi import Depends
from fastapi import HTTPException, status
from petowners.domain.models.petOwner import PetOwner
from pets.domain.models.pet import Pet
from medicalhistory.interfaces.rest.resources.medicalHistory import MedicalHistorySchemaPost
from pets.interfaces.rest.resources.pet import PetSchemaPost, PetSchemaResponse
from medicalhistory.domain.services.medical_history import MedicalHistoryService
from SmartCollar.Application.Schema.smart_collar_schema import SmartCollarRequest
from SmartCollar.Application.Services.smart_collar_service import SmartCollarService
from SmartCollar.Domain.ValueObject.location_type import LocationType
class PetServices:
    @staticmethod
    def create_new_pet(petowner_id: int, pet: PetSchemaPost, db: Session ):
        pet_owner = db.query(PetOwner).filter(PetOwner.userId == petowner_id).first()
        if not pet_owner:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El propietario de la mascota no existe.")

        if pet.weight <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El peso debe ser mayor a 0.")


        new_pet = Pet(petOwnerId=pet_owner.id,
                      name=pet.name,
                      birthdate=pet.birthdate,
                      weight=pet.weight,
                      species=pet.species,
                        breed=pet.breed,
                        gender= pet.gender,
                        image_url= pet.image_url)
        db.add(new_pet)
        db.commit()
        db.refresh(new_pet)  # Para cargar el ID generado
        
        ser = "upet-"
        if(new_pet.id < 100):
            ser += "0"
        if(new_pet.id < 10):
            ser += "0"
        ser += str(new_pet.id)
        
        smartCollar = SmartCollarRequest(
            serial_number=ser,
            temperature = 0.0,
            lpm = 0.0,
            battery = 100.0,
            location = LocationType(latitude=0.0, longitude=0.0)
        )
        SmartCollarService.add_smart_collar(smartCollar)
        SmartCollarService.change_pet_association(new_pet.id,new_pet.id)

        medicalHistory = MedicalHistorySchemaPost(
            petId=new_pet.id,
            date=datetime.date.today(),
            description=f"Creación de historial médico de {new_pet.name}"
        )
        MedicalHistoryService.add_medical_history(medicalHistory,db=db)
        return new_pet


    @staticmethod
    def get_pet_by_user_id(pet_id: int, db: Session):
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        return pet

    @staticmethod
    def get_pets_by_petOwnerid(petOwner_id: int, db: Session):
        pets = db.query(Pet).filter(Pet.petOwnerId == petOwner_id).all()
        return pets

    @staticmethod
    def update_pet(pet_id: int, pet: PetSchemaPost, db: Session):
        pet_db = db.query(Pet).filter(Pet.id == pet_id).first()
        if not pet_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada")

        PetSchemaResponse.update_pet_from_schema(pet_db, pet)
        db.commit()
        return pet_db

    @staticmethod
    def get_pet_by_id(pet_id: int, db: Session):
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if not pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
        return pet

    @staticmethod
    def delete_pet(pet_id: int, db: Session):
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if not pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada")
        db.delete(pet)
        db.commit()
        return pet

    @staticmethod
    def get_petowners(db: Session):
        pet = db.query(Pet)
        if not pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pets not found")
        return pet
