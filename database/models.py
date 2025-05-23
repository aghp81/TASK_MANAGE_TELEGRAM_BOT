# models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False, index=True)
    username = Column(String)
    full_name = Column(String)

    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    assigned_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="tasks")

    phases = relationship("Phase", back_populates="task", cascade="all, delete-orphan")


class Phase(Base):
    __tablename__ = 'phases'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    name = Column(String, nullable=False)
    progress = Column(Float, default=0.0)

    task = relationship("Task", back_populates="phases")
