from sqlalchemy import Column, Integer, String, Text
from src.db.database import Base

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(Text)
    profile_picture = Column(String(255))
    user_id = Column(Integer, unique=True, nullable=False)  # FK a User