from sqlalchemy import Column, Integer, String
from src.database import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    year = Column(Integer, unique=True, index=True)