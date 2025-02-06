from src.db.database import get_mongo_db
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

# Cargar variables de entorno
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Configuración de Cloudinary
cloudinary.config( 
    cloud_name=f"{os.getenv('CLOUDINARY_CLOUD')}",
    api_key=f"{os.getenv('CLOUDINARY_API_KEY')}",
    api_secret=f"{os.getenv('CLOUDINARY_API_SECRET')}",
    secure=True
)

def create_piece_img(piece_img_data: dict, image_file):
    # Subir la imagen a Cloudinary
    upload_result = cloudinary.uploader.upload(image_file, public_id=piece_img_data["name"])
    image_url = upload_result["secure_url"]

    # Guardar la URL de la imagen en MongoDB
    db = get_mongo_db()
    piece_img_data["file_url"] = image_url  # Añadir la URL de la imagen al diccionario
    result = db.piece_img.insert_one(piece_img_data)
    return str(result.inserted_id)

def get_piece_img(piece_img_id: str):
    db = get_mongo_db()
    return db.piece_img.find_one({"_id": piece_img_id})

def get_all_piece_imgs(
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    sort_by: str = None
):
    db = get_mongo_db()
    query = filter_by if filter_by else {}
    cursor = db.piece_img.find(query).skip(skip).limit(limit)

    if sort_by:
        cursor = cursor.sort(sort_by)

    return list(cursor)

def update_piece_img(piece_img_id: str, piece_img_data: dict):
    db = get_mongo_db()
    result = db.piece_img.update_one(
        {"_id": piece_img_id},
        {"$set": piece_img_data}
    )
    return result.modified_count > 0

def delete_piece_img(piece_img_id: str):
    db = get_mongo_db()
    result = db.piece_img.delete_one({"_id": piece_img_id})
    return result.deleted_count > 0