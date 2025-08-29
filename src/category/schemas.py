from pydantic import BaseModel

class CategoryCreate(BaseModel):
    color: str
    seats: int

class Category(BaseModel):
    id: int
    color: str
    year: int

    class Config:
        orm_mode = True