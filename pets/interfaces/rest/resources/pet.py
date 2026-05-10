from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date
from pets.domain.models.speciesEnum import SpecieEnum
from pets.domain.models.genderEnum import GenderEnum
from pets.domain.models.pet import Pet

_DEFAULT_PET_IMAGE = "https://image.freepik.com/vector-gratis/ilustracion-vector-dibujos-animados-lindo-animal-mascota_24640-53565.jpg"

class PetSchemaPost(BaseModel):
    name: str
    breed: str
    species: SpecieEnum
    weight: float = Field(..., gt=0)
    birthdate: date
    image_url: Optional[str] = _DEFAULT_PET_IMAGE
    gender: GenderEnum

class PetSchemaResponse(BaseModel):
    id: int
    name: str
    petOwnerId: int
    breed: str
    species: SpecieEnum
    weight: float
    birthdate: date  
    image_url: str
    gender: GenderEnum
    
    class Config:
        from_attributes = True

    @classmethod
    def from_orm(cls, pet: Pet):
        return cls(
            id = pet.id,
            name = pet.name,
            petOwnerId = pet.petOwnerId,
            breed = pet.breed,
            species = pet.species,
            weight = pet.weight,
            birthdate = pet.birthdate,
            image_url = pet.image_url,
            gender = pet.gender
        )
    
    @classmethod
    def update_pet_from_schema(cls, pet: Pet, pet_schema: PetSchemaPost):
        pet.name = pet_schema.name
        pet.breed = pet_schema.breed
        pet.species = pet_schema.species
        pet.weight = pet_schema.weight
        pet.birthdate = pet_schema.birthdate
        pet.image_url = pet_schema.image_url
        pet.gender = pet_schema.gender
        return pet