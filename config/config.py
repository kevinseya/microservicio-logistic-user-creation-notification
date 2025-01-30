import os
from dotenv import load_dotenv

load_dotenv()

#Config MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "notificaciones_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "notificaciones")

#Config email smtp
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "tu_email@gmail.com")  # Reemplaza con tu email
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "tu_password")  # Reemplaza con tu contraseña
MAIL_USE_TLS = True
MAIL_USE_SSL = False
