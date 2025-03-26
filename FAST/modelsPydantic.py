
from pydantic import BaseModel, Field, EmailStr


class modelousuario(BaseModel):

    name:str  = Field(...,min_length=3,max_length=84,description="Solo letras entre: min 3 max 85")#queremos que tenga un nombre minimo de 3 y el maximo de 85
    age:int = Field(...,gt= 1, lt=100, description="La edad tiene que ser en numero positivo y entre ")
    email:EmailStr = Field(..., description="Correo electrónico válido")

class modeloAuth(BaseModel):
    correo: EmailStr = Field(..., description="Correo electrónico válido")
    passw:str = Field (..., min_length=8, strip_whitespace=True, description="Contraseña minimo 8 caracteres")