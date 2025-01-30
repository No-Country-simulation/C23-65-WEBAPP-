from src.db.database import get_mongo_db

def create_artpiece_genres(artpiece_genres_data: dict):
    db = get_mongo_db()
    result = db.artpiece_genres.insert_one(artpiece_genres_data)
    return str(result.inserted_id)

def get_artpiece_genres(artpiece_genres_id: str):
    db = get_mongo_db()
    return db.artpiece_genres.find_one({"_id": artpiece_genres_id})

def update_artpiece_genres(artpiece_genres_id: str, artpiece_genres_data: dict):
    db = get_mongo_db()
    result = db.artpiece_genres.update_one(
        {"_id": artpiece_genres_id},
        {"$set": artpiece_genres_data}
    )
    return result.modified_count > 0

def delete_artpiece_genres(artpiece_genres_id: str):
    db = get_mongo_db()
    result = db.artpiece_genres.delete_one({"_id": artpiece_genres_id})
    return result.deleted_count > 0