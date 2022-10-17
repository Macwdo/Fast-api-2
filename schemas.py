from typing import List, Optional
from pydantic import BaseModel, Field, validator
from security import criacao, verificacao


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    
class UsuarioPatch(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    hash_password: Optional[str] = Field(alias='senha')
    
    @validator('hash_password', pre=True)
    def hash_senha_create(cls, v):
        return criacao(v)


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    hash_password: str = Field(alias='senha')
    
    @validator('hash_password', pre=True)
    def hash_senha_create(cls, v):
        return criacao(v)

class UsuarioVerify(BaseModel):
    email: str
    senha: str
    
    @validator("senha",pre=True)
    def hash_senha_verify(cls, v):
        return verificacao(v)
        

class ProdutoSCHM(BaseModel):
    id: int
    usuario: int
    nome: str 
    detalhes: str 
    preco: float 
    disponivel: bool
    
class ProdutoSCHMPatch(BaseModel):
    nome:Optional[str] = None
    detalhes:Optional[str] = None
    preco: Optional[float] = None
    disponivel: Optional[bool] = None
    
    
class PedidosSCHM(BaseModel):
    id: int
    usuario: int
    quantidade: int
    entrega: bool
    endereco: str
    obs: Optional[str]