from datetime import datetime, timedelta
import jwt
import smtplib
from email.mime.text import MIMEText

class AuthenticationService:
    SECRET_KEY = "seu_segredo_jwt"
    
    @classmethod
    def generate_token(cls, user_id: int) -> str:
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        return jwt.encode(payload, cls.SECRET_KEY, algorithm="HS256")
    
    @classmethod
    def verify_token(cls, token: str) -> dict:
        try:
            payload = jwt.decode(token, cls.SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token expirado"}
        except jwt.InvalidTokenError:
            return {"error": "Token inválido"}
    
    @classmethod
    def send_password_reset_email(cls, user_email: str, reset_token: str):
        reset_link = f"https://seusite.com/reset-password?token={reset_token}"
        
        msg = MIMEText(f"Clique no link para redefinir sua senha: {reset_link}")
        msg['Subject'] = "Redefinição de Senha"
        msg['From'] = "noreply@seusite.com"
        msg['To'] = user_email
        
        # Configuração do servidor SMTP
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login("seuemail@gmail.com", "sua_senha")
        smtp_server.send_message(msg)
        smtp_server.quit()
