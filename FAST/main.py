from fastapi import FastAPI, HTTPException,Depends 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 
from typing import Optional,List
from modelsPydantic import modelousuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session,engine,Base
from models.modelsDB import User



app= FastAPI(
    title= 'Mi primer API S192',
    description='Daniela Valdez',
    version='1.0.1'
    )
#modelo de validaciones 

Base.metadata.create_all(bind=engine)


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




#Autenticacion
@app.post('/Auth/', tags=['Autentificacion'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'Daniela@example.com' and autorizacion.passw =='123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(token)
    else:
        return{"Aviso":"Usuario sin autorizacion"}




#Consulta ususario 
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    db = Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error al guardar el usuario",
                "usuario": str(e)
            })
    
    finally:
        db.close#cerramos las conecxiones de la bd 



#Consulta ususario id 
@app.get('/usuario/{id}', tags=['Operaciones CRUD'])
def buscarUno(id:int):
    db = Session()
    try:
        consultauno= db.query(User).filter(User.id == id).first()
        if not consultauno:
            return JSONResponse(status_code="404", content={"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consultauno))
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error al consultar",
                "usuario": str(e)
            })
    
    finally:
        db.close #cerramos las conecxiones de la bd 
   
   

#agregar usuario
@app.post('/usuario/', response_model=modelousuario, tags=['Operaciones CRUD'])
def agregarusuarios(usuario: modelousuario):
    db = Session()  # definimos esta variable para que se vaya todo a la db
    try: 
        db.add(User(**usuario.model_dump()))  # para hacer el insert  
        db.commit()  # confirmamos el cambio 
        return JSONResponse(
            status_code=201,
            content={
                "message": "Usuario Guardado",
                "usuario": usuario.model_dump()  # corregido aquí
            }
        )  # cuando se hace exitosamente el insert
    except Exception as e:  # para hacer excepciones en la bd 
        db.rollback()  # en caso de que falle 
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error al guardar el usuario",
                "usuario": str(e)
            }
        )
    finally:
        db.close()
        


#Editar Usuario 
@app.put('/usuario/{id}',response_model=modelousuario, tags=['Operaciones CRUD'])
def actualizarusuario (id:int, usuarioActualizado:modelousuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        usuario.name = usuarioActualizado.name
        usuario.age = usuarioActualizado.age
        usuario.email = usuarioActualizado.email

        db.commit()
        return JSONResponse(status_code=200, 
                            content={
                                "message":"Usuario Actualizado", 
                                "usuario": jsonable_encoder(usuario)})
    

    except Exception as e:
        db.rollback()  
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error al actualizar el usuario",
                "error": str(e)
            })
        

    finally:
        db.close()

    



#Elimiar usuario 
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarusuario(id: int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db.delete(usuario)  
        db.commit() 
        return {"detail": "Usuario eliminado exitosamente"}
    
    except Exception as e:
        db.rollback()  
        return JSONResponse(
            status_code=500,
            content={
                "message": "Error al eliminar el usuario",
                "error": str(e)
            }
        )
    
    finally:
        db.close()  
