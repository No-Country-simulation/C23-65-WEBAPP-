from src.db.database import get_mongo_db

def create_piece_img(piece_img_data: dict):
    db = get_mongo_db()
    result = db.piece_img.insert_one(piece_img_data)
    return str(result.inserted_id)

def get_piece_img(piece_img_id: str):
    db = get_mongo_db()
    return db.piece_img.find_one({"_id": piece_img_id})

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