from pydantic import BaseModel

class SaleCreate(BaseModel):
    stock: int

class Sale(BaseModel):
    id: int
    stock: int

    class Config:
        orm_mode = True