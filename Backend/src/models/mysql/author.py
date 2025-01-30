from sqlalchemy import Column, Integer, String, Date
from src.db.database import Base

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    birth_date = Column(Date)
    death_date = Column(Date)
    nationality = Column(String(255))