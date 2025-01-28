from pydantic import BaseModel
from typing import List
from datetime import datetime
from bson import ObjectId

# Modelo de Gallery_artpiece
class GalleryArtpieceInDB(BaseModel):
    id: str
    gallery_id: str
    artpiece_id: str
    note: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)

# Modelo de Artpiece_styles
class ArtpieceStylesInDB(BaseModel):
    id: str
    style_id: str
    artpiece_id: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)

# Modelo de Artpiece_genres
class ArtpieceGenresInDB(BaseModel):
    id: str
    artpiece_id: str
    genre_id: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)

# Modelo de Piece_img
class PieceImgInDB(BaseModel):
    id: str
    file: str  # Guarda el archivo en base64 o URI
    name: str
    archeopiece_id: str
    artpiece_id: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)

# Modelo de Profile_following
class ProfileFollowingInDB(BaseModel):
    id: str
    from_profile_id: str
    to_profile_id: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)

# Modelo de Archeopiece
class ArcheopieceInDB(BaseModel):
    id: str
    name: str
    object_type: str
    production_date: str
    material: str
    technique: str
    dimensions: str
    description: str
    findspot: str
    current_location: str
    culture_period_id: str

    @classmethod
    def from_mongo(cls, mongo_data: dict):
        mongo_data["id"] = str(mongo_data["_id"])
        del mongo_data["_id"]
        return cls(**mongo_data)
