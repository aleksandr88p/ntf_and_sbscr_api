import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional




class SubscrionBase(BaseModel):
    name: str
    price: float
    start_date: datetime.datetime
    duration_days: int
    is_trial: bool = False

class SubscriptionCreate(SubscrionBase):
    pass

class SubscriptionRead(SubscrionBase):
    id: int
    end_date: datetime.datetime
    model_config = ConfigDict(from_attributes=True)

class SubscriptionUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    is_trial: Optional[bool] = None
    duration_days: Optional[int] = None
    price: Optional[float] = None


    
