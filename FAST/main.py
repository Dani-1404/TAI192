from fastapi import FastAPI 
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


@app.get('promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 6.1

@app.get('/usuario/{id}', tags=['parametro obligatorio'])
def consultaUsuario(id:int):
    #conectamos a ala BD
    #consultamos
    return {'Se encontro el usuario':id}

    
    
    #Endopint parametro Opcional
@app.get('/usuario/', tags=['Parametro opcional'])
def consultaUsuario1(id: Optional[int]=None): 

    if id is not None: #validamos que exite id
        for usu in usuarios: #si exite comienso interar 
            if usu["id"] == id: #pasamos el parametro 
                return {"Mensaje":"Usuario encontrado","usuario": usu} #Y regresamos el mensaje si esta pasando 
         
        return {"Mensaje":f"No se encontro el usuario con id : {id}"}#Y regresamos el mensaje si no esta pasando 
    else :
        return {'No se proporciono un Id':id}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}

