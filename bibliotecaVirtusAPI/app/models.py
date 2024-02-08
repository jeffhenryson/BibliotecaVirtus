# app/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .config import SQLALCHEMY_DATABASE_URL

# Instância base para os modelos declarativos do SQLAlchemy
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    primeiro_nome = Column(String, index=True)  # Adicionado
    segundo_nome = Column(String, index=True)   # Adicionado
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

