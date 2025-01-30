from sqlalchemy import Column, Integer, DateTime
from src.db.database import Base

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    archeopiece_id = Column(Integer)  # FK a Archeopiece (MongoDB)
    artpiece_id = Column(Integer)  # FK a Artpiece
    gallery_id = Column(Integer)  # FK a Gallery
    user_id = Column(Integer)  # FK a User