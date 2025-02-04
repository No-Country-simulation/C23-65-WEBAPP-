from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Configuración de SQLAlchemy
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASS')}@"
    f"{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "ssl_ca":os.path.join(BASEDIR, 'ca.pem'),
        "connect_timeout": 30,
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Configuración de MongoDB
MONGO_DATABASE_URL = (
    f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@"
    f"{os.getenv('MONGO_HOST')}/?retryWrites=true&w=majority&appName=pocketmuseum-nocountry"
)
mongo_client = MongoClient(MONGO_DATABASE_URL)
mongo_db = mongo_client["pocketmuseum"]

# Crear tablas en MySQL (si no existen)
def create_tables():
    Base.metadata.create_all(bind=engine)

# Crear colecciones en MongoDB (si no existen)
def create_collections():
    collections = [
        "gallery_artpiece",
        "artpiece_styles",
        "artpiece_genres",
        "piece_img",
        "profile_following",
        "archeopiece"
    ]
    for collection in collections:
        if collection not in mongo_db.list_collection_names():
            mongo_db.create_collection(collection)

# Inicializar la base de datos
def init_db():
    create_tables()  # Crear tablas en MySQL
    create_collections()  # Crear colecciones en MongoDB

# Obtener la sesión de MySQL
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener la conexión a MongoDB
def get_mongo_db():
    return mongo_db