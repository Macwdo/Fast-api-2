import ormar
from configs.database import metadata, database
from models.usuario import Usuario

class Produto(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Produto'
        
    id: int = ormar.Integer(primary_key=True,autoincrement=True)
    nome: str = ormar.String(max_length=30)
    vendedor: int = ormar.ForeignKey(
        Usuario,
        skip_reverse=True
        )
    detalhes: str = ormar.String(max_length=60)
    preco: float = ormar.Float()
    disponivel: bool = ormar.Boolean(default=False)
    


        
    