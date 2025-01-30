from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Artpiece(Base):
    __tablename__ = "artpiece"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    year = Column(Integer)
    dimension = Column(String(255))
    author_id = Column(Integer)  # FK a Author
    medium_id = Column(Integer)  # FK a Medium