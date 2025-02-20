from fastapi import FastAPI, HTTPException 
from typing import Optional,List
from pydantic import BaseModel


app= FastAPI(
    title= 'Mi primer API S192',
    description='Daniela Valdez',
    version='1.0.1'
    )
#modelo de validaciones 
class modelousuario(BaseModel):
    id:int
    nombre:str
    edad:int
    correo:str
    


#BD ficticia
usuarios=[
        {"id": 1,"nombre":"Daniela", "edad":24,"correo":"example@example.com"},
        {"id": 2,"nombre":"Diana", "edad":23,"correo":"example@example.com"},
        {"id": 3,"nombre":"Ivet", "edad":21,"correo":"example@example.com"},
        {"id": 4,"nombre":"Belen", "edad":20,"correo":"example@example.com"}
    ]

#Endpoint home 
@app.get('/', tags=['Hola Mundo'])
def home():
    return{'hello':'world FastApi'}

#Consulta ususario 
@app.get('/todosUsuarios',response_model=list[modelousuario], tags=['Operaciones CRUD'])
def leerUsuarios():
    return{"Los usuaruarios resgistrados son":usuarios}


#Agregar usuario 
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarusuarios (usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"): 
            raise HTTPException(status_code=400, detail="El id ya existe")   
    usuarios.append(usuario)
    return usuario
#Editar Usuario 
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarusuario (id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#Elimiar usuario 

@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarusuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index] 
            return {"detail": "Usuario eliminado exitosamente"}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
