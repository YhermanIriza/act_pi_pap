from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from .schemas import Car, CarCreate
from .models import Car as CarModel

router = APIRouter()

# POST - Crear
@router.post("/cars/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = CarModel(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# GET - Listar todos
@router.get("/cars/", response_model=list[Car])
def get_cars(db: Session = Depends(get_db)):
    return db.query(CarModel).all()

# GET - Buscar por ID
@router.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

# PUT - Actualizar
@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    for key, value in car.dict().items():
        setattr(db_car, key, value)
    db.commit()
    db.refresh(db_car)
    return db_car

# DELETE - Eliminar
@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(db_car)
    db.commit()
    return {"mensaje": "Car eliminado"}
