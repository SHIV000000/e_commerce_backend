# auth_service/utils.py

import jwt

SECRET_KEY = "your_secret_key"

def generate_token(user_id):
    token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
