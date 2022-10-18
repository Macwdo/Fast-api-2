# from typing import List, Optional
# import ormar
# from schemas import PedidosSCHM, UsuarioSCH, ProdutoSCHM
# from configs.database import database, metadata
#
# class Usuario(ormar.Model):
#     class Meta:
#         metadata = metadata
#         database = database
#         tablename = 'Usuario'
        
#     id: int = ormar.Integer(primary_key=True,autoincrement=True)
#     nome: str = ormar.String(max_length=30)
#     email: str = ormar.String(max_length=100)
#     senha: str = ormar.String(max_length=64)
#     pedidos: Optional[List[PedidosSCHM]]
#     produto: Optional[List[ProdutoSCHM]]
    
    
# class Produto(ormar.Model):
#     class Meta:
#         metadata = metadata
#         database = database
#         tablename = 'Produto'
        
#     id: int = ormar.Integer(primary_key=True,autoincrement=True)
#     usuario: UsuarioSCH = ormar.ForeignKey(Usuario)
#     nome: str = ormar.String(max_length=30)
#     detalhes: str = ormar.String(max_length=60)
#     preco: float = ormar.Float()
#     disponivel: bool = ormar.Boolean(default=False)

    
# class Pedido(ormar.Model):
#     class Meta:
#         metadata = metadata
#         database = database
#         tablename = 'Pedido'
        
#     id: int = ormar.Integer(primary_key=True,autoincrement=True)
#     usuario: Usuario = ormar.ForeignKey(Usuario)
#     quantidade: int = ormar.Integer()
#     entrega: bool = ormar.Boolean(default=False)
#     endereco: str = ormar.String(max_length=40)
#     obs: Optional[str] = ormar.String(max_length=90,default="Sem observação")

    
    