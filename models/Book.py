from sqlalchemy import Column, Integer, String, Table
from config.db import Base, engine

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    field_1 = Column(String)
    author = Column(String)
    description = Column(String)
    my_numeric_field= Column(Integer) 

Base.metadata.create_all(bind=engine)
