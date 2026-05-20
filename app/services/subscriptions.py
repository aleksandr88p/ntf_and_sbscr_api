
# Логика: CRUD + автовычисление end_date + проверка владельца
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.subscriptions import Subscription
from app.schemas.subscriptions import SubscriptionCreate, SubscriptionUpdate
from datetime import datetime, timedelta

def calculate_end_date(start_date: datetime, duration_days: int) -> datetime:
    return start_date + timedelta(days=duration_days)


async def create_subscription(session: AsyncSession, subscription_data: SubscriptionCreate, user_id: int):
    start_date = subscription_data.start_date
    duration_days = subscription_data.duration_days
    end_date = calculate_end_date(start_date, duration_days)

    subscription_object = Subscription(
        name=subscription_data.name,
        price=subscription_data.price,
        start_date=start_date,
        duration_days=duration_days,
        end_date=end_date,
        is_trial=subscription_data.is_trial,
        user_id=user_id,
    )
    
    session.add(subscription_object)
    await session.commit()
    await session.refresh(subscription_object)
    
    return subscription_object
    

async def get_subscription(session: AsyncSession, subscription_id: int, user_id: int):
    result = await session.execute(select(Subscription).where(Subscription.id == subscription_id, Subscription.user_id == user_id))
    return result.scalar_one_or_none()

async def get_user_subscriptions(session: AsyncSession, user_id: int):
    result = await session.execute(select(Subscription).where(Subscription.user_id == user_id))
    return result.scalars().all()


async def update_subscription(session: AsyncSession, subscription_id: int, user_id: int, subscription_data_to_update: SubscriptionUpdate):
    subscription = await get_subscription(session, subscription_id, user_id)
    if not subscription:
        return None
    
    for field, value in subscription_data_to_update.model_dump(exclude_unset=True).items():
        setattr(subscription, field, value)
    
    await session.commit()
    await session.refresh(subscription)
    
    return subscription

 
   
async def delete_subscription(session: AsyncSession, subscription_id: int, user_id: int):
    subscription = await get_subscription(session, subscription_id, user_id)
    if not subscription:
        return None
    
    await session.delete(subscription)
    await session.commit()
    
    return subscription