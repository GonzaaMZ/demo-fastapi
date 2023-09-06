from jwt import encode, decode, exceptions
from fastapi import HTTPException
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse
from models.User import User

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def write_token(data: str):
    new_data = dict({"data": data})
    token = encode(payload={**new_data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    return JSONResponse(content={"token": token}, status_code=200)


def validate_token(token, output=False):
    if(token is None):
        raise HTTPException(status_code=401, detail="Token is empty")
    try:
        if output:
           return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token expired"}, status_code=401)
    except exceptions.PyJWKError:
        return JSONResponse(content={"message": "Token is empty"}, status_code=401)
