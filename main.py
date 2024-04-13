from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tobias(BaseModel):
    nombre: str
    apellido: str
    edad: int
    dni: int

@app.get("/")
def index():
    return {"msj" : "Hola soy un Ñoqui"}

@app.get("/getinfo")
def mostrar_info(Persona : Tobias):
    return {"tobias" : f"Nombre : {Persona.nombre},\nApellido : {Persona.apellido}"}