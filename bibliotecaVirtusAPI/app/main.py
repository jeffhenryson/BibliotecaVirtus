from fastapi import FastAPI, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserResponse
from .models import User
from .utils import get_password_hash, authenticate_user, create_access_token
from .dependencies import get_db
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
    form_data = await request.json()
    email = form_data.get("email")
    password = form_data.get("password")
    authentication_result = authenticate_user(db, email, password)

    if authentication_result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="E-mail não registrado."
        )
    elif isinstance(authentication_result, str) and authentication_result == "password_incorrect":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta, tente novamente."
        )
    elif not isinstance(authentication_result, User):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro na autenticação."
        )
    else:
        user = authentication_result

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
