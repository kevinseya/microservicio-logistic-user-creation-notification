from flask import Flask, request, jsonify
from model.model import Notificacion
from repository.repository import save_notification
from service.email_service import send_email
from uuid import UUID
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook_create_user", methods=["POST"])
def webhook():
    """
    Endpoint to recive notifications on webhook, and sent mail.
    """
    try:
        data = request.json
        data["user_id"] = UUID(data["user_id"])  
        data["date"] = datetime.utcnow()  

        #Save on database
        notification = save_notification(data)

        #Sent mail
        email_sent = send_email(
            recipient=data["email"],
            subject="Notificación de Creación de Usuario",
            body=f"Hola {data['name']} {data['lastname']},\n\nTu rol asignado es: {data['role']}\n\n{data['message']}\n\nSaludos."
        )

        if email_sent:
            return jsonify({"message": "Notification recived and mail sent", "data": notification}), 201
        else:
            return jsonify({"message": "Notification recived and fail mail sent", "data": notification}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
