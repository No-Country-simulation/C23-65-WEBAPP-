from src.db.database import get_mongo_db

def create_gallery_artpiece(gallery_artpiece_data: dict):
    db = get_mongo_db()
    result = db.gallery_artpiece.insert_one(gallery_artpiece_data)
    return str(result.inserted_id)

def get_gallery_artpiece(gallery_artpiece_id: str):
    db = get_mongo_db()
    return db.gallery_artpiece.find_one({"_id": gallery_artpiece_id})

def get_all_gallery_artpieces(
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    sort_by: str = None
):
    db = get_mongo_db()
    query = filter_by if filter_by else {}
    cursor = db.gallery_artpiece.find(query).skip(skip).limit(limit)

    if sort_by:
        cursor = cursor.sort(sort_by)

    return list(cursor)

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