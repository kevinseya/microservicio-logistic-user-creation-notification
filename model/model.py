from datetime import datetime
from pydantic import BaseModel, EmailStr
from uuid import UUID

class Notificacion(BaseModel):
    user_id: UUID
    name: str
    lastname: str
    email: EmailStr
    message: str
    date: datetime

    def to_dict(self):
        return {
            "user_id": str(self.user_id), 
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "message": self.message,
            "date": self.date.isoformat()
        }
