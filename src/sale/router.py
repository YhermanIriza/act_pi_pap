from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from .schemas import Sale, SaleCreate
from .models import Sale as SaleModel

router = APIRouter()

# POST - Crear
@router.post("/sales/", response_model=Sale)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = SaleModel(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# GET - Listar todos
@router.get("/sales/", response_model=list[Sale])
def get_sales(db: Session = Depends(get_db)):
    return db.query(SaleModel).all()

# GET - Buscar por ID
@router.get("/sales/{sale_id}", response_model=Sale)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

# PUT - Actualizar
@router.put("/sales/{sale_id}", response_model=Sale)
def update_sale(sale_id: int, sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if not db_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    for key, value in sale.dict().items():
        setattr(db_sale, key, value)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# DELETE - Eliminar
@router.delete("/sales/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if not db_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    db.delete(db_sale)
    db.commit()
    return {"mensaje": "Sale eliminado"}
