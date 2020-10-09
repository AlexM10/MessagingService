from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    username = Column(String(64), index=True, unique=True, nullable=False, primary_key=True)
    password_hash = Column(String(128), nullable=False)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    sender = Column(Integer, ForeignKey("user.username"), nullable=False)
    receiver = Column(Integer, ForeignKey("user.username"), nullable=False)
    subject = Column(String(250), nullable=False)
    message = Column(String(1500), nullable=False)
    timestamp = Column(DateTime, index=True, default=datetime.now())
    is_read = Column(Boolean, unique=False, default=False)
    sender_user = relationship("User", foreign_keys=[sender])
    receiver_user = relationship("User", foreign_keys=[receiver])
