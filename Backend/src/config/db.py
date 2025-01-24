from sqlalchemy import create_engine, MetaData


# URL de conexion a MySQL
engine = create_engine("mysql+pymysql://root:Adm1n25*/@localhost:3306/museum_db")

meta = MetaData()

# La configuracion de SQLAlchemy
conn = engine.connect()