"""User model using classic SQLAlchemy syntax."""
from sqlalchemy import Boolean, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from .base import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(500), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now()
    )
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"