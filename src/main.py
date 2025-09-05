from fastapi import FastAPI
from src.car.router import router as car_router
from src.category.router import router as category_router
from src.sale.router import router as sale_router
from src.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el router de usuarios
app.include_router(car_router, prefix="/api", tags=["car"])
app.include_router(category_router, prefix="/api", tags=["category"])
app.include_router(sale_router, prefix="/api", tags=["sale"])

origins = [
    "http://localhost:3000",  # frontend Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],           # permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],           # permitir todas las cabeceras
)