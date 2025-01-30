from src.db.database import get_mongo_db

def create_gallery_artpiece(gallery_artpiece_data: dict):
    db = get_mongo_db()
    result = db.gallery_artpiece.insert_one(gallery_artpiece_data)
    return str(result.inserted_id)

def get_gallery_artpiece(gallery_artpiece_id: str):
    db = get_mongo_db()
    return db.gallery_artpiece.find_one({"_id": gallery_artpiece_id})

def update_gallery_artpiece(gallery_artpiece_id: str, gallery_artpiece_data: dict):
    db = get_mongo_db()
    result = db.gallery_artpiece.update_one(
        {"_id": gallery_artpiece_id},
        {"$set": gallery_artpiece_data}
    )
    return result.modified_count > 0

def delete_gallery_artpiece(gallery_artpiece_id: str):
    db = get_mongo_db()
    result = db.gallery_artpiece.delete_one({"_id": gallery_artpiece_id})
    return result.deleted_count > 0