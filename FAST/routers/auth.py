
from fastapi.responses import JSONResponse
from modelsPydantic import modelousuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from fastapi import APIRouter


RouterAuth = APIRouter()
#Autenticacion

@RouterAuth.post('/Auth/', tags=['Autentificacion'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'Daniela@example.com' and autorizacion.passw =='123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(token)
    else:
        return{"Aviso":"Usuario sin autorizacion"}
