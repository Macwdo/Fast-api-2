# note this is just a partial snippet full working example below
# 1. Imports
import sqlalchemy
import databases
import ormar

# 2. Initialization
DATABASE_URL = "sqlite:///ecommerce.sqlite"
TESTE_DATABASE = False
database = databases.Database(DATABASE_URL, force_rollback=TESTE_DATABASE)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.drop_all(engine)
metadata.create_all(engine)
