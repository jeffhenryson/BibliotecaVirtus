# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from .schemas import UserCreate, UserResponse
from .models import User
from .utils import get_password_hash, authenticate_user, create_access_token
from .dependencies import get_db
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

# Configuração CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "*",  # Isso permite todas as origens. Em produção, você deve considerar apenas as origens específicas.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.post("/login")
async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
    form_data = await request.json()
    email = form_data.get("email")
    password = form_data.get("password")
    user = authenticate_user(db, email, password)  # Autenticar o usuário usando e-mail e senha

        # Se as credenciais estiverem erradas (usuário não encontrado ou senha incorreta)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais erradas, tente novamente."
        )

    # Se o usuário não for encontrado pelo e-mail ou a senha estiver incorreta
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email não registrado, faça cadastro para conseguir acessar o site."
        )

    # Geração do token de acesso
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"message": f"Bem-vindo {user.username}", "access_token": access_token, "token_type": "bearer"}


@app.post("/cadastro", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    # Verifique se o nome de usuário já existe
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Verifique se o e-mail já existe
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
        
    hashed_password = get_password_hash(user.password)
    
    db_user = User(
        username=user.username, 
        primeiro_nome=user.primeiro_nome,  
        segundo_nome=user.segundo_nome,    
        email=user.email, 
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Personalize a mensagem de boas-vindas com o primeiro nome do usuário
    welcome_message = f"Bem vindo {db_user.primeiro_nome}, estamos feliz em ter você aqui como contribuidor do acervo literário virtual Biblioteca Virtus."
    
    # Retorne o usuário e a mensagem personalizada
    return UserResponse(user=db_user, message=welcome_message)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
