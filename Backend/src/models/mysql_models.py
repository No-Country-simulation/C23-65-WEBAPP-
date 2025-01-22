from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

class PieceImg(Base):
    __tablename__ = "piece_img"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)
    archepiece_id = Column(Integer, ForeignKey("archepiece.id"), nullable=True)
    artpiece_id = Column(Integer, ForeignKey("artpiece.id"), nullable=True)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)
    mime_type = Column(String(50))
    file_size = Column(Integer)
