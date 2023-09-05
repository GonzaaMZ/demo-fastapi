from pydantic import BaseModel

class BookCreate(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int


class BookResponse(BaseModel):
    id: int
    field_1: str
    author: str
    description: str
    my_numeric_field: int