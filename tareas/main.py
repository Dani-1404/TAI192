from fastapi import FastAPI, HTTPException 
from typing import Optional


app = FastAPI(
    title='API de Gestión de Tareas',
    description='API para gestionar una lista de tareas',
    version='1.0.0'
)

tareas=[
        {"id": 1,"titulo":"Estudiar para el examen","Descripcion":"Repasar los apuntes de TAI ", "Vencimiento":"14-02-24", "Estado":"Completado"},
        {"id": 2,"nombre":"Diana", "edad":23},
        {"id": 3,"nombre":"Ivet", "edad":21},
        {"id": 4,"nombre":"Belen", "edad":20}
    ]