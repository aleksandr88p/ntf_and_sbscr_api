from sqlalchemy import Column, Integer
from app.models.base import Base
from datetime import datetime
from sqlalchemy import DateTime

class User(Base):
    __tablename__="nts_users"

    telegram_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
       


