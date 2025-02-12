from fastapi import FastAPI, HTTPException 
from typing import Optional


app= FastAPI(
    title= 'Mi primer API S192',
    description='Daniela Valdez',
    venrsion='1.0.1'
    )

usuarios=[
        {"id": 1,"nombre":"Daniela", "edad":24},
        {"id": 2,"nombre":"Diana", "edad":23},
        {"id": 3,"nombre":"Ivet", "edad":21},
        {"id": 4,"nombre":"Belen", "edad":20}
    ]

#Endpoint home 
@app.get('/', tags=['Hola Mundo'])
def home():
    return{'hello':'world FastApi'}

#Consulta ususario 
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
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

@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarusuario (id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            # Actualiza el usuario con los nuevos datos
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    
    # Si no se encuentra el usuario, lanza una excepción
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

