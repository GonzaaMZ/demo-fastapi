from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

def userEntity(item) -> dict:
    return {
        "id": str(item["id"]),
        "username": item["username"],
        "email": item["email"],
        "password": item["password"]
    }