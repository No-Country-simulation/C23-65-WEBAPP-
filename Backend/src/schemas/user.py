from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
 id: Optional[int] = None
 name: str
 last_name: str
 password: str
 nationality: str
 email: str