from src.db.database import get_mongo_db

def create_profile_following(profile_following_data: dict):
    db = get_mongo_db()
    result = db.profile_following.insert_one(profile_following_data)
    return str(result.inserted_id)

def get_profile_following(profile_following_id: str):
    db = get_mongo_db()
    return db.profile_following.find_one({"_id": profile_following_id})

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