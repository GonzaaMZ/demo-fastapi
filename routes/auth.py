from fastapi import APIRouter, HTTPException, Header
from schemas.User import UserCreate, UserLogin, userEntity
from passlib.hash import sha256_crypt
from passlib.context import CryptContext
from config.db import SessionLocal
from models.User import User
from helpers.jwt_helper import write_token, validate_token

 

auth_routes = APIRouter()

context = CryptContext(schemes=["bcrypt", "sha256_crypt"], deprecated="auto")

def verify_password(plane_password, hashed_password):
    return context.verify(plane_password, hashed_password)

@auth_routes.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not exist")
    
    if verify_password(user.password, user_db.password ) is False:
        raise HTTPException(status_code=404, detail="Password Incorrect")

    db.close()
    return write_token(user_db.email)


@auth_routes.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    new_user = User(**new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return "user created"

@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)