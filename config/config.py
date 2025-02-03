import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://adminuser:adminpassword@3.83.119.45/notificaciones_create_user?authSource=admin")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "notificaciones_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "notificaciones")

MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "tu_email@gmail.com")  
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "tu_password")  
MAIL_USE_TLS = True
MAIL_USE_SSL = False
