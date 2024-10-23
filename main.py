from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario,Gasto,Categoria,MetodoPago,Base
from app.api.routes.rutas import rutas
from starlette.responses import RedirectResponse

#ACTIVAR EL ORM
Base.metadata.create_all(bind=engine)

#variable para administrar la aplicacion
app=FastAPI()

#ACTIVO EL API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)