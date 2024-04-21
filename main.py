from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Alonso(BaseModel):
    nombre: str
    apellido: str
    edad: int
    dni: int

@app.get("/")
def index():
    return {"msj" : "Hola soy un Ñoqui"}

@app.get("/getinfo")
def mostrar_info(Persona : Alonso):
    return {"Piloto" : f"Nombre : {Persona.nombre},\nApellido : {Persona.apellido}"}

@app.get("/sumar")
def sumar(a: int, b: int):
    return a + b

@app.get("/restar")
def restar(a: int, b: int):
    return a - b

@app.get("/multiplicar")
def multiplicar(a: int, b: int):
    return a * b

@app.get("/dividir")
def dividir(a: int, b: int):
    return a / b