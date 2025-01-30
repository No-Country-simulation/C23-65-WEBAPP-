from sqlalchemy import Column, Integer, Text, DateTime
from src.db.database import Base

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)  # FK a User
    gallery_id = Column(Integer, nullable=False)  # FK a Gallery