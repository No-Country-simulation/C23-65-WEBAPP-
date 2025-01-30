from sqlalchemy import Column, Integer, String, Text, DateTime
from src.db.database import Base

class Gallery(Base):
    __tablename__ = "gallery"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    description = Column(Text)
    created_at = Column(DateTime, nullable=False)
    owner_id = Column(Integer, nullable=False)  # FK a User