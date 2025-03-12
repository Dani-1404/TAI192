from fastapi import FastAPI, HTTPException 
from models import BaseModel
from pydantic import BaseModel

app= FastAPI(
    title= 'Mi Examen API S192',
    description='Daniela Valdez',
    venrsion='1.0.1'
    )

class modelousuario(BaseModel):
    Nlicencia:int
    nombre:str
    Tlicencia:str

usuarios=[
        {"nombre":"Daniela", "Tipo de licencia":"A", "No.licencia": 123456789101},
        {"nombre":"Ana", "Tipo de licencia":"B", "No.licencia": 123456789102},
        {"nombre":"Horacio", "Tipo de licencia":"C", "No.licencia": 123456789103}
        
    ]

#consultar conductores
@app.get('/todosUsuarios',response_model=modelousuario, tags=['Consultar Usuarios'])
def leerUsuarios():
    return{"Los usuaruarios resgistrados son":usuarios}

#editar conductor

@app.put('/usuario/{Nlicencia}',response_model=modelousuario, tags=['Editar Conductor'])
def actualizarusuario (Nlicencia:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["No.licencia"] == Nlicencia:
           
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]