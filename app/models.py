from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Autograph(Base):
    __tablename__="autograph"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    contact = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    hometown = Column(String(150), nullable=False)
    note = Column(Text)