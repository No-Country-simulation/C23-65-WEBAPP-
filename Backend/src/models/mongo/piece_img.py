from pydantic import BaseModel
from typing import Optional

class PieceImg(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId
    file: bytes  # Archivo binario
    name: str
    archeopiece_id: Optional[int]  # FK a Archeopiece
    artpiece_id: Optional[int]  # FK a Artpiece