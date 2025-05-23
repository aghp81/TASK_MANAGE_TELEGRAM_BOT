# models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    assigned_to = Column(String)  # می‌تونه آیدی تلگرام کاربر باشه
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    phases = relationship("Phase", back_populates="task", cascade="all, delete-orphan")

class Phase(Base):
    __tablename__ = 'phases'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    name = Column(String, nullable=False)
    progress = Column(Float, default=0.0)

    task = relationship("Task", back_populates="phases")
