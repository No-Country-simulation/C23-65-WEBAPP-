from sqlalchemy import Column, Integer, String
from src.db.database import Base

class CulturePeriod(Base):
    __tablename__ = "culture_period"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)