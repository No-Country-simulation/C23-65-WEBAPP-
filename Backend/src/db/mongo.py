# mongo.py

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["museum_database"]

# Inicializar colecciones
collections = [
    "profile_following",
    "gallery_artpiece",
    "artpiece_styles",
    "artpiece_genres",
    "piece_images",
    "archeopieces"
]

async def initialize_collections():
    # Obtener las colecciones existentes en la base de datos
    existing_collections = await db.list_collection_names()

    # Crear las colecciones si no existen
    for collection_name in collections:
        if collection_name not in existing_collections:
            await db.create_collection(collection_name)
            print(f"Collection {collection_name} created.")
        else:
            print(f"Collection {collection_name} already exists.")

# Función para obtener la base de datos
def get_mongo_db():
    return db

# Cerrar la conexión de MongoDB
def close_mongo_connection():
    client.close()
    print("MongoDB connection closed.")
