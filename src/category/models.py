from sqlalchemy import Column, Integer, String
from src.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, unique=True, index=True)
    seats = Column(Integer, unique=True, index=True)