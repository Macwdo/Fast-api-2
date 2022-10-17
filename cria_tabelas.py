import sqlalchemy

from configs.database import DATABASE_URL, metadata
from models.prod import Produto
from models.usuario import Usuario

def configurar(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
if __name__ == "__main__":
    configurar()