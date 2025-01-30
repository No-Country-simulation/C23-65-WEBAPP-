from pydantic import BaseModel
from typing import Optional

class ProfileFollowing(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId
    from_profile_id: int  # FK a Profile en MySQL
    to_profile_id: int  # FK a Profile en MySQL