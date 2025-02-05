from src.db.database import get_mongo_db

def create_archeopiece(archeopiece_data: dict):
    db = get_mongo_db()
    result = db.archeopiece.insert_one(archeopiece_data)
    return str(result.inserted_id)

def get_archeopiece(archeopiece_id: str):
    db = get_mongo_db()
    return db.archeopiece.find_one({"_id": archeopiece_id})

def get_all_archeopieces(
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    sort_by: str = None
):
    db = get_mongo_db()
    query = filter_by if filter_by else {}
    cursor = db.archeopiece.find(query).skip(skip).limit(limit)

    if sort_by:
        cursor = cursor.sort(sort_by)

    return list(cursor)

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