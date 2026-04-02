from cryptography.fernet import Fernet
import jwt
import os
from datetime import datetime, timedelta

class SecurityManager:
    def __init__(self):
        self.key = os.getenv("ENCRYPTION_KEY", Fernet.generate_key())
        self.fernet = Fernet(self.key)
        self.jwt_secret = os.getenv("JWT_SECRET", "agent-demo-secret")

    def encrypt(self, text: str) -> str:
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, token: str) -> str:
        return self.fernet.decrypt(token.encode()).decode()

    def mask_phone(self, phone: str) -> str:
        if len(phone) >= 7:
            return phone[:3] + "****" + phone[-4:]
        return "***"

    def create_token(self, user_id: str):
        return jwt.encode({
            "user": user_id,
            "exp": datetime.utcnow() + timedelta(days=1)
        }, self.jwt_secret, algorithm="HS256")