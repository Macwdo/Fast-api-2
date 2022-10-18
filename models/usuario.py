from typing import List
import ormar
import re
from pydantic import Json, validator
from configs.database import metadata, database

cargos = ["vendedor","comprador","admin"]

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "Usuario"
        
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)
    hash_password: str = ormar.String(max_length=255)
    cargos: Json = ormar.JSON(default=[])


    @validator('email')
    def valida_email(cls,v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('Formato de email invalido')
        return v    

    @validator('cargos')
    def valida_cargos(cls,v):
        if not isinstance(v,list):
            raise ValueError(f"Os Cargo do usuario deve ser uma lista")
        for cargo in v:
            if not isinstance(cargo, str) or cargo not in cargos:
                raise ValueError(f"A Cargo {cargo} não existe")
        return v

    @validator('cargos')
    def valida_cargos_duplicados(cls,v):
        return list(set(v))

