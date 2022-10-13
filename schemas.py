from email.policy import default
from typing import List, Optional
import ormar
from configs.database import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Usuario'
    
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=70)
    email: str = ormar.String(max_length=15, unique=True)
    meus_produtos: List[Produto] = ormar.ManyToMany(Produto)
    minhas_vendas: List[Pedido] = ormar.ManyToMany(Pedido)
    meus_pedidos: List[Pedido] = ormar.ManyToMany(Pedido)


class Produto(BaseModel):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Produto'
        
    id: int = ormar.Integer(primary_key=True,autoincrement=True)
    usuario: Usuario = ormar.ForeignKey(Usuario)
    nome: str = ormar.String(max_length=30)
    detalhes: str = ormar.String(max_length=60)
    preco: float = ormar.Float()
    disponivel: bool = ormar.Boolean(default=False)
    

class Pedido(BaseModel):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Pedido'
        
    id: int = ormar.Integer(primary_key=True,autoincrement=True)
    usuario: Usuario = ormar.ForeignKey(Usuario)
    produto: Produto = ormar.ForeignKey(Produto)
    quantidade: int = ormar.Integer()
    entrega: bool = ormar.Boolean(default=False)
    endereco: str = ormar.String(max_length=40)
    obs: Optional[str] = ormar.String(max_length=90,default="Sem observação")
    
    
    
    