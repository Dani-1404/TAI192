
from pydantic import BaseModel, Field, EmailStr


class modelousuario(BaseModel):
    id:int = Field(...,gt=0,description="Id unico y solo numeros positivos") #queremos que sea un numero mayor a 0 y una descripcion
    nombre:str  = Field(...,min_length=3,max_length=84,description="Solo letras entre: min 3 max 85")#queremos que tenga un nombre minimo de 3 y el maximo de 85
    edad:int = Field(...,gt= 1, lt=100, description="La edad tiene que ser en numero positivo y entre ")
    correo:EmailStr = Field(..., description="Correo electrónico válido")