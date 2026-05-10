from fastapi import APIRouter

from auth.interfaces.rest.user import users as user_router
from veterinaryclinics.interfaces.rest.veterinaryClinic import veterinary_clinics as veterinary_clinic_router
from pets.interfaces.rest.pet import pets as pet_router
from appointments.interfaces.rest.appointment import appointments as appointment_router
from notifications.interfaces.rest.notification import notifications as notification_router
from medicalhistory.interfaces.rest.medicalHistory import medical_histories as medical_history_router
from petowners.interfaces.rest.petOwner import pet_owners as pet_owner_router
from veterinarian.interfaces.rest.veterinarian import veterinarians as veterinarian_router
from medicalhistory.interfaces.rest.disease import diseases as disease_router
from medicalhistory.interfaces.rest.vaccination import vaccinations as vaccine_router
from reviews.interfaces.rest.review import reviews as review_router
from appointments.interfaces.rest.availability import availabilities as availability_router
from auth.interfaces.rest.auth import auth as auth_router
from medicalhistory.interfaces.rest.pdfReport import pdf_router as pdf_router
from petowners.interfaces.rest.favorite_clinics import favorite_clinics as favorite_clinics_router
from config.routes import prefix
from notifications.interfaces.rest.reminder import reminders as reminder_router
routes = APIRouter()

# Include all the routes
routes.include_router(auth_router,  prefix= prefix)
routes.include_router(user_router, prefix= prefix)
routes.include_router(veterinary_clinic_router,  prefix= prefix)
routes.include_router(pet_router,  prefix= prefix)
routes.include_router(appointment_router,  prefix= prefix)
routes.include_router(notification_router,  prefix= prefix, tags=["Notifications"])
routes.include_router(medical_history_router,  prefix= prefix)
routes.include_router(pet_owner_router,  prefix= prefix)
routes.include_router(veterinarian_router, prefix= prefix)
routes.include_router(disease_router, prefix= prefix)
routes.include_router(vaccine_router,  prefix= prefix)
routes.include_router(review_router,  prefix= prefix)
routes.include_router(availability_router,  prefix= prefix)
routes.include_router(pdf_router, prefix= prefix, tags=["PDF Reports"])
routes.include_router(favorite_clinics_router, prefix= prefix)
routes.include_router(reminder_router, prefix=prefix, tags=["Reminders"])