from sqlalchemy import Column, Integer, String
from src.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    stock = Column(Integer, unique=True, index=True)