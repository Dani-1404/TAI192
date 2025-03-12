from pydantic import BaseModel, Field


class modelousuario(BaseModel):
    Nlicencia:int = Field(...,gt=0,min_length=12,max_length=12,description="Id unico y solo numeros positivos") #queremos que sea un numero mayor a 0 y una descripcion
    nombre:str  = Field(...,min_length=3,max_length=84,description="Solo letras entre: min 3 max 85")#queremos que tenga un nombre minimo de 3 y el maximo de 85
    Tlicencia:str = Field(...,max_length=1, description="Solo tiene que ser una Una letra A,B,C o D ")