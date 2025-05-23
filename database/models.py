from sqlalchemy import Column, Integer, String
from database.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, default="member")  # admin / member / supervisor
