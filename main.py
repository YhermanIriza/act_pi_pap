from fastapi import FastAPI
from src.car.router import router as car_router
from src.category.router import router as category_router
from src.sale.router import router as sale_router
from src.database import Base, engine

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el router de usuarios
app.include_router(car_router, prefix="/api", tags=["car"])
app.include_router(category_router, prefix="/api", tags=["category"])
app.include_router(sale_router, prefix="/api", tags=["sale"])