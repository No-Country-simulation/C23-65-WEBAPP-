from src.db.database import get_mongo_db

def create_profile_following(profile_following_data: dict):
    db = get_mongo_db()
    result = db.profile_following.insert_one(profile_following_data)
    return str(result.inserted_id)

def get_profile_following(profile_following_id: str):
    db = get_mongo_db()
    return db.profile_following.find_one({"_id": profile_following_id})

def get_all_profile_following(
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    sort_by: str = None
):
    db = get_mongo_db()
    query = filter_by if filter_by else {}
    cursor = db.profile_following.find(query).skip(skip).limit(limit)

    if sort_by:
        cursor = cursor.sort(sort_by)

    return list(cursor)

def update_profile_following(profile_following_id: str, profile_following_data: dict):
    db = get_mongo_db()
    result = db.profile_following.update_one(
        {"_id": profile_following_id},
        {"$set": profile_following_data}
    )
    return result.modified_count > 0

def delete_profile_following(profile_following_id: str):
    db = get_mongo_db()
    result = db.profile_following.delete_one({"_id": profile_following_id})
    return result.deleted_count > 0