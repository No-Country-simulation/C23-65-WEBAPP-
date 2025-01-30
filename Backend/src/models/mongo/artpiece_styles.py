from pydantic import BaseModel
from typing import Optional

class GalleryArtpiece(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId
    gallery_id: int  # FK a Gallery en MySQL
    artpiece_id: int  # FK a Artpiece en MySQL
    note: Optional[str]