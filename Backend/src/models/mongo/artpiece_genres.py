from pydantic import BaseModel
from typing import Optional

class ArtpieceGenres(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId
    artpiece_id: int  # FK a Artpiece en MySQL
    genre_id: int  # FK a Genre en MySQL