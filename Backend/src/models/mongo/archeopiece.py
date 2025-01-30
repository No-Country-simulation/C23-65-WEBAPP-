from pydantic import BaseModel
from typing import Optional

class Archeopiece(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId
    name: str
    object_type: str
    production_date: str
    material: str
    technique: str
    dimensions: str
    description: str
    findspot: str
    current_location: str
    culture_period_id: int  # FK a CulturePeriod en MySQL