# app/utils.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from .config import SECRET_KEY, ALGORITHM
from .models import User
from sqlalchemy.orm import Session

# Instância do CryptContext para hash e verificação de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar uma senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para obter o hash de uma senha
def get_password_hash(password):
    return pwd_context.hash(password)

# Função para autenticar o usuário
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

# Função para criar um novo token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
