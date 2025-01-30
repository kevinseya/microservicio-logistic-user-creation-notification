import os
from flask import Flask, request, jsonify
from model.model import Notificacion
from repository.repository import save_notification
from service.email_service import send_email
from uuid import UUID
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

port = int(os.getenv("PORT", 5000))

@app.route("/")
def home():
    return f"Webhook is running on port {port} 🚀"

@app.route("/webhook_create_user", methods=["POST"])
def webhook():
    """
    Endpoint to receive notifications on webhook and send email.
    """
    try:
        data = request.json
        data["user_id"] = UUID(data["user_id"])  
        data["date"] = datetime.utcnow()  

        # Save on database
        notification = save_notification(data)

        # Send email
        email_sent = send_email(
            recipient=data["email"],
            subject="Notificación de Creación de Usuario",
            body=f"Hola {data['name']} {data['lastname']},\n\nTu rol asignado es: {data['role']}\n\n{data['message']}\n\nSaludos."
        )

        if email_sent:
            return jsonify({"message": "Notification received and mail sent", "data": notification}), 201
        else:
            return jsonify({"message": "Notification received but mail failed to send", "data": notification}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print(f"Webhook is running on port {port} 🚀") 
    app.run(debug=True, host="0.0.0.0", port=port)
