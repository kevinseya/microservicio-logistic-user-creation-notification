from config.database import db
from config.config import MONGO_COLLECTION
from model.model import Notificacion

collection = db[MONGO_COLLECTION]

def save_notification(data):
    """
    Save notification on MongoDB and return object insert.
    """
    notification = Notificacion(**data)
    result = collection.insert_one(notification.to_dict())
    return {"_id": str(result.inserted_id), **notification.to_dict()}
