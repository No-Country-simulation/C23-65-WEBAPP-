from sqlalchemy import Column, Integer, DateTime
from src.db.database import Base

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer)  # FK a User
    gallery_id = Column(Integer)  # FK a Gallery