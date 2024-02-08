# app/schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Esquema para receber dados de usuário na criação
class UserCreate(BaseModel):
    username: str = Field(..., example="johndoe")
    primeiro_nome: str = Field(..., example="John")  
    segundo_nome: str = Field(..., example="Doe")    
    email: EmailStr = Field(..., example="johndoe@example.com")
    password: str = Field(..., example="strongpassword")

# Esquema para representar um usuário já criado, sem a senha
class UserOut(BaseModel):
    id: int
    username: str
    primeiro_nome: str
    segundo_nome: str 
    email: EmailStr

    class Config:
        from_attributes = True
        
class UserResponse(BaseModel):
    user: UserOut
    message: str

# Esquema para dados de login do usuário
class UserLogin(BaseModel):
    email: EmailStr 
    password: str

# Esquema para o token de acesso JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Esquema para os dados do token
class TokenData(BaseModel):
    username: Optional[str] = None
