from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Medium(Base):
    __tablename__ = "medium"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)