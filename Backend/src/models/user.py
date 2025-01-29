from sqlalchemy import Column, Integer, String
from config.db import Base

# Definiendo la Structura
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    nationality = Column(String)