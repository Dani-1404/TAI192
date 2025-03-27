from fastapi import FastAPI, HTTPException,Depends 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 
from modelsPydantic import modelousuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter



routerUsuario = APIRouter()
#Consulta ususario 
@routerUsuario.get('/todosUsuarios', tags=['Operaciones CRUD'])
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
@routerUsuario.get('/usuario/{id}', tags=['Operaciones CRUD'])
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
@routerUsuario.post('/usuario/', response_model=modelousuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuario/{id}',response_model=modelousuario, tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuario/{id}', tags=['Operaciones CRUD'])
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
