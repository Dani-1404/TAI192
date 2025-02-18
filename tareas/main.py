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
@app.get('/Mostrar_Tareas', tags=['Operaciones Tareas'])
def leertareas():
    return{"Las tareas resgistradas son":tareas}

#Consultar tarea po ID
@app.get('/Consultar_Tarea/{tarea_id}', tags=['Operaciones Tareas'])
def obtener_tarea(tarea_id: int):
    tarea_encontrada = next((tarea for tarea in tareas if tarea["id"] == tarea_id), None)
    if tarea_encontrada:
        return tarea_encontrada
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#Agregar tarea 
@app.post('/Agregar_Tarea/', tags=['Operaciones Tarea'])
def agregartareas (tarea:dict):
    for tarea in tareas:
        if tarea["id"] == tarea.get("id"): 
            raise HTTPException(status_code=400, detail="El id ya existe")   
    tareas.append(tarea)
    return tarea

#Actualizar tarea
@app.put('/Tareas/{id}', tags=['Operaciones tareas'])
def actualizartarea (id:int, tareaActualizado:dict):
    for index, usr in enumerate(tareas):
        if usr["id"] == id:
            tareas[index].update(tareaActualizado)
            return tareas[index]
    
    raise HTTPException(status_code=404, detail="Tarea no encontrado")

#Eliminar tarea
@app.delete('/Eliminar Tarea/{id}', tags=['Operaciones Tareas'])
def eliminartarea(id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            del tareas[index] 
            return {"detail": "Tarea eliminada exitosamente"}
    
    raise HTTPException(status_code=404, detail="Tarea no encontrada")