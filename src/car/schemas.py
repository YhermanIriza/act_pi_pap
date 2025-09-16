from pydantic import BaseModel

class CarCreate(BaseModel):
    model: str
    year: int

class Car(BaseModel):
    id: int
    model: str
    year: int

    class Config:
        orm_mode = True