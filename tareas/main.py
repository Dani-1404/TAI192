from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title='API de Gestión de Tareas',
    description='API para gestionar una lista de tareas',
    version='1.0.0'
)

class Tarea(BaseModel):
    id: int
    titulo: str
    Descripcion: str
    Vencimiento: str
    Estado: str

tareas: List[Tarea] = [
    Tarea(id=1, titulo="Estudiar para el examen", Descripcion="Repasar los apuntes de TAI", Vencimiento="14-02-24", Estado="Completado"),
    Tarea(id=2, titulo="Estudiar para la Exposición", Descripcion="Repasar los apuntes de diseño de interfaces", Vencimiento="20-02-24", Estado="En proceso"),
    Tarea(id=3, titulo="Realizar Práctica", Descripcion="Realizar Práctica de Tecnologías de Virtualización", Vencimiento="03-03-24", Estado="En Pendiente"),
]

# Consultar tareas
@app.get('/Mostrar_Tareas', tags=['Mostrar Tareas'])
def leertareas():
    return {"Las tareas registradas son": tareas}

# Consultar tarea por ID
@app.get('/Consultar_Tarea/{tarea_id}', tags=['Consultar tarea'])
def obtener_tarea(tarea_id: int):
    tarea_encontrada = next((tarea for tarea in tareas if tarea.id == tarea_id), None)
    if tarea_encontrada:
        return tarea_encontrada
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Agregar tarea 
@app.post('/Agregar_Tarea/', tags=['Agregar tarea'])
def agregartareas(tarea: Tarea):
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="El id ya existe")
    tareas.append(tarea)
    return tarea

# Actualizar tarea
@app.put('/Tareas/{id}', tags=['Actualizar tarea'])
def actualizartarea(id: int, tareaActualizado: Tarea):
    for index, tarea in enumerate(tareas):
        if tarea.id == id:
            tareas[index] = tareaActualizado
            return tareas[index]
    
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Eliminar tarea
@app.delete('/Eliminar_Tarea/{id}', tags=['Eliminar tarea'])
def eliminartarea(id: int):
    for index, tarea in enumerate(tareas):
        if tarea.id == id:
            del tareas[index]
            return {"detail": "Tarea eliminada exitosamente"}
    
    raise HTTPException(status_code=404, detail="Tarea no encontrada")