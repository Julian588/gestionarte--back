from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.database.configuration import sessionLocal, engine
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion,GastoDTORespuesta,CategoriaDTOPeticion,CategoriaDTORespuesta,MetodoPagoDTOPeticion,MetodoPagoDTORespuesta
from app.api.models.modelosApp import Usuario, Gasto, Categoria,MetodoPago


#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios",
response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario {error}")


@rutas.post("/gastos",
response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion,db:Session=Depends(getDataBase)):
    try:
        gasto=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto {error}")
    

@rutas.post("/categoria", 
response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcionCategoria=datosPeticion.descripcionCategoria,
            fotoIcono=datosPeticion.fotoIcono
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la categoria {error}")
    

@rutas.post("/metodopago", response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        metodoPago=MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcionMetodoPago=datosPeticion.descripcionMetodoPago
        )
        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return metodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el metodopago {error}")
    
@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios (db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener el usuario {error}")

@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGasto (db:Session=Depends(getDataBase)):
    try:
        listadoDeGasto=db.query(Gasto).all()
        return listadoDeGasto
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener el gasto {error}")
    
@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta])
def buscarCategoria (db:Session=Depends(getDataBase)):
    try:
        listadoDeCategoria=db.query(Categoria).all()
        return listadoDeCategoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener la categoria {error}")
    
@rutas.get("/metodopago", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago (db:Session=Depends(getDataBase)):
    try:
        listadoDeMetodoPago=db.query(MetodoPago).all()
        return listadoDeMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener el metodopago {error}")