from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
from auth.domain.models.subscriptionTypeEnum import SubscriptionType
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class PetOwner(Base):
    __tablename__ = 'petowners'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'))
    numberPhone = Column(String(9))
    location = Column(String(150))
    subscriptionType = Column(Enum(SubscriptionType, name='subscription_type'), default=SubscriptionType.Basic)

    user = relationship("User", back_populates="pet_owner") 
    pets = relationship("Pet", back_populates="pet_owner", cascade="all, delete-orphan")    
    reviews = relationship('Review', back_populates='petowner')  # Relación con Review

from auth.domain.models.user import User
from reviews.domain.models.review import Review
