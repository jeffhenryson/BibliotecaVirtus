# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()


# Chave secreta para a criação de tokens JWT. Deve ser obtida da variável de ambiente.
SECRET_KEY = os.getenv('SECRET_KEY', 'uma_chave_secreta_muito_segura_para_desenvolvimento')

# Algoritmo de criptografia para JWT
ALGORITHM = "HS256"

# Tempo de validade do token de acesso
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# URI do banco de dados para conexão SQLAlchemy
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL', 'fallback_default_sqlalchemy_database_url')
