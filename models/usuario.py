import ormar
import re
from pydantic import validator
from configs.database import metadata, database

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "Usuario"
        
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)
    hash_password: str = ormar.String(max_length=255)
    
    @validator('email')
    def valida_email(cls,v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('Formato de email invalido')
        return v    