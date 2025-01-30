from src.db.database import get_mongo_db

def create_artpiece_styles(artpiece_styles_data: dict):
    db = get_mongo_db()
    result = db.artpiece_styles.insert_one(artpiece_styles_data)
    return str(result.inserted_id)

def get_artpiece_styles(artpiece_styles_id: str):
    db = get_mongo_db()
    return db.artpiece_styles.find_one({"_id": artpiece_styles_id})

def update_artpiece_styles(artpiece_styles_id: str, artpiece_styles_data: dict):
    db = get_mongo_db()
    result = db.artpiece_styles.update_one(
        {"_id": artpiece_styles_id},
        {"$set": artpiece_styles_data}
    )
    return result.modified_count > 0

def delete_artpiece_styles(artpiece_styles_id: str):
    db = get_mongo_db()
    result = db.artpiece_styles.delete_one({"_id": artpiece_styles_id})
    return result.deleted_count > 0