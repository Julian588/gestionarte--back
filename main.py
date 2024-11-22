from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario,Gasto,Categoria,MetodoPago,Base
from app.api.routes.rutas import rutas
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


#ACTIVAR EL ORM
Base.metadata.create_all(bind=engine)

#variable para administrar la aplicacion
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

#ACTIVO EL API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)