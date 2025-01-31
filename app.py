import os
from flask import Flask, request, jsonify
from model.model import Notificacion
from repository.repository import save_notification
from service.email_service import send_email
from uuid import UUID
from datetime import datetime
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure, WriteError


load_dotenv()

app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

@app.route("/")
def home():
    return f"Webhook is running on port {port} 🚀"

@app.route("/test-db")
def test_db():
    try:
        from config.database import db
        db[os.getenv("MONGO_COLLECTION")].find_one()
        return jsonify({"message": "Connection to MongoDB succesfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Error of connection: {str(e)}"}), 500

@app.route("/webhook_create_user", methods=["POST"])
def webhook():
    """
    Endpoint to receive notifications on webhook and send email.
    """
    try:
        if not request.is_json:
            return jsonify({"error": "Se requiere contenido JSON"}), 400

        data = request.json
        
        required_fields = ["user_id", "name", "lastname", "email", "message", "role"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Required field missing: {field}"}), 400

        data["user_id"] = UUID(data["user_id"])  
        data["date"] = datetime.utcnow()  
        
        try:
            notification = save_notification(data)
            
        except (ConnectionFailure, WriteError) as e:
            return jsonify({"error": f"Error of database: {str(e)}"}), 503
        
        email_sent = send_email(
            recipient=data["email"],
            subject="Notificación de Creación de Usuario",
            body=f"Hola {data['name']} {data['lastname']},\n\n"
                 f"Tu rol asignado es: {data['role']}\n\n"
                 f"{data['message']}\n\n"
                 "Saludos."
        )
        
        response = {
            "message": "Notification received and mail sent" if email_sent else "Notification received but mail failed to send",
            "data": notification,
            "email_status": "sent" if email_sent else "failed"
        }
        
        return jsonify(response), 201
            
    except ValueError as e:
        return jsonify({"error": f"Error de validación: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    print(f"Webhook is running on port {port} 🚀")
    app.run(debug=True, host="0.0.0.0", port=port)