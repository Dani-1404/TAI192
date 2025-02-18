from fastapi import FastAPI, HTTPException 
from typing import Optional


app = FastAPI(
    title='API de Gestión de Tareas',
    description='API para gestionar una lista de tareas',
    version='1.0.0'
)

tareas=[
        {"id": 1,"titulo":"Estudiar para el examen","Descripcion":"Repasar los apuntes de TAI ", "Vencimiento":"14-02-24", "Estado":"Completado"},
        {"id": 2,"titulo":"Estudiar para la Expocision","Descripcion":"Repasar los apuntes de diseño de interfaces ", "Vencimiento":"20-02-24", "Estado":"En proceso"},
        {"id": 3,"titulo":"Realizar Practica","Descripcion":"Realizar Practica de Tecnologias de Virtualizacion ", "Vencimiento":"03-003-24", "Estado":"En Pendiente"},
    ]


#Consultar tareas
@app.get('/todostareas', tags=['Operaciones CRUD'])
def leertareas():
    return{"Las tareas resgistradas son":tareas}
