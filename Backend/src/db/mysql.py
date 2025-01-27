# mysql.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.mysql_models import Base

DATABASE_URL = "mysql+mysqlconnector://root:admin1234@localhost/museumrdb"

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_mysql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para inicializar la conexión y crear las tablas
def initialize_connection():
    try:
        # Intenta conectar y crear las tablas si no existen
        with engine.connect() as connection:
            Base.metadata.create_all(bind=engine)  # Esto creará las tablas
            print("MySQL connection initialized and tables created successfully")
    except Exception as e:
        print(f"Error initializing MySQL connection: {e}")
        raise

# Cerrar la conexión de MySQL
def close_connection():
    # Cerrar la conexión en el pool (opcional si SQLAlchemy maneja esto automáticamente)
    with engine.connect() as connection:
        connection.close()
    print("MySQL connection closed.")
