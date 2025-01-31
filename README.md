# WEBHOOK in Python with Flask

This is project is a simple WEBHOOK create with Flask that allows managing the NOTIFICATION domain microservice. This project offers the basic operation such as notify of the creation of user.
## Project Structure

- **`app.py`**: The main class that runs the Flask application and defines the notification.

- `POSTT /webhook_create_user`: Allows access to the functionality that allows the notification to be executed


## Requeriments

- Python 3.x
- Flask
- An SMTP service account to send emails

## Installation


### 1. Clona el repositorio

```bash
https://github.com/kevinseya/microservicio-logistic-user-creation-notification.git
```
### 2. Create a Virtual Environment.
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install depedencies.
```bash
pip install -r requirements.txt
```
### 4. Run the Application Locally.
Start the Flask application on your local machine:
```bash
python app.py
```
### 5. The application run on `http://localhost:5000`.

## Use of Webhook.

###  POST /webhook_create_user Content-Type: application/json
```json
    {
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "John",
    "lastname": "Doe",
    "email": "john.doe@example.com",
    "role": "ADMIN",
    "message": "User created successfully"
    }
```
**Response**
- **`201 Created:`** Notification processed succesfully, email sent.
```plaintext
    {
    "message": "Notification received and mail sent",
        "data": {
            "_id": "some_mongo_id",
            "user_id": "550e8400-e29b-41d4-a716-446655440000",
            "name": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "role": "ADMIN",
            "message": "User created successfully",
            "date": "2025-01-30T00:00:00Z"
        }
    }
```
- **`201 Created:`** Notification processed successfully, but email sending failed.
```plaintext
    {
    "message": "Notification received but mail failed to send",
        "data": {
            "_id": "some_mongo_id",
            "user_id": "550e8400-e29b-41d4-a716-446655440000",
            "name": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "role": "ADMIN",
            "message": "User created successfully",
            "date": "2025-01-30T00:00:00Z"
        }
    }
```
- **`400 Bad Request:`** Invalid input or error processing the request.
