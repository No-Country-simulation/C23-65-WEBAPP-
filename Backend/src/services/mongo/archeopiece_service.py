from src.db.database import get_mongo_db

def create_archeopiece(archeopiece_data: dict):
    db = get_mongo_db()
    result = db.archeopiece.insert_one(archeopiece_data)
    return str(result.inserted_id)

def get_archeopiece(archeopiece_id: str):
    db = get_mongo_db()
    return db.archeopiece.find_one({"_id": archeopiece_id})

def update_archeopiece(archeopiece_id: str, archeopiece_data: dict):
    db = get_mongo_db()
    result = db.archeopiece.update_one(
        {"_id": archeopiece_id},
        {"$set": archeopiece_data}
    )
    return result.modified_count > 0

def delete_archeopiece(archeopiece_id: str):
    db = get_mongo_db()
    result = db.archeopiece.delete_one({"_id": archeopiece_id})
    return result.deleted_count > 0