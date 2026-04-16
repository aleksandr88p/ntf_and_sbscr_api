from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from app.models.base import Base
from sqlalchemy import DateTime


class Subscription(Base):
    __tablename__="nts_subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("nts_users.telegram_id"), index=True)
    name = Column(String, index=True)
    price = Column(Float)
    start_date = Column(DateTime)
    duration_days = Column(Integer)
    end_date = Column(DateTime)
    is_trial = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    



