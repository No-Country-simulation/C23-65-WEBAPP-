from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ImageMetadata(BaseModel):
    file_name: str
    mime_type: str
    file_size: int
    upload_date: datetime

class Archepiece(BaseModel):
    id: str
    title: str
    object_type: str
    images: List[ImageMetadata]
