from fastapi import APIRouter, HTTPException
from schemas.Book import BookCreate, BookResponse
from config.db import SessionLocal
from models.Book import Book
from fastapi.responses import JSONResponse
from middlewares.verify_token_route import VerifyTokenRoutes

router = APIRouter(route_class=VerifyTokenRoutes)

@router.post("/input/{my_target_field}", response_model=dict)
def create_book( book: BookCreate, my_target_field: str):
    db = SessionLocal()
    field_uppercase: str
    print(my_target_field)
    if my_target_field == "field-1":
        field_uppercase = book.field_1.upper()
        book.field_1 = field_uppercase
    elif my_target_field == "author":
        field_uppercase = book.author.upper()
        book.author = field_uppercase
    elif my_target_field == "description":
        field_uppercase = book.description.upper()
        book.description = field_uppercase
    elif my_target_field == "my_numeric_field":
        raise HTTPException(status_code=400, detail="my_numeric_field no es un campo válido para convertir a mayúscula")
    else:
        raise  HTTPException(status_code=400, detail=my_target_field + " no es un campo válido para convertir a mayúscula")
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()
    return JSONResponse(content={"id": new_book.id})

@router.get("/get-data/{id}")
def get_data(id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == id).first()
    db.close()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book