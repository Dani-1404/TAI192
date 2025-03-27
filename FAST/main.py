from fastapi import FastAPI, HTTPException,Depends 
from DB.conexion import engine,Base
from routers.usuario import routerUsuario
from routers.auth import RouterAuth




app= FastAPI(
    title= 'Mi primer API S192',
    description='Daniela Valdez',
    version='1.0.1'
    )


#modelo de validaciones 
Base.metadata.create_all(bind=engine)


#Endpoint home 
@app.get('/', tags=['Hola Mundo'])
def home():
    return{'hello':'world FastApi'}

app.include_router(routerUsuario)
app.include_router(RouterAuth)