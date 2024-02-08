# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from .schemas import UserCreate, Token, UserOut, UserLogin
from .models import User
from .utils import get_password_hash, authenticate_user, create_access_token
from .dependencies import get_db
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import Response
from fastapi import Request



app = FastAPI()

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




@app.post("/cadastro", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
