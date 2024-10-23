from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#GASTO
class Gasto(Base):
    __tablename__='gasto'
    id=Column(Integer,primary_key=True, autoincrement=True, nullable=False, unique=True)
    monto=Column(Integer,nullable=False)
    fecha=Column(Date,nullable=False)
    descripcion=Column(String(200),nullable=False)
    nombre=Column(String(50),nullable=False) 

#CATEGORIA
class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nombreCategoria=Column(String(50), nullable=False)
    descripcionCategoria=Column(String(200), nullable=False)
    fotoIcono=Column(String(500), nullable=False)

#METODOS DE PAGO
class MetodoPago(Base):
    __tablename__='metodoPago'
    id=Column(Integer, primary_key=True, nullable=False, unique=True)
    nombreMetodo=Column(String(30), nullable=False)
    descripcionMetodoPago=Column(String(200), nullable=False)

#FACTURA
# class Factura(Base):
#     pass