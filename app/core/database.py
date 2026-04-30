from app.core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.models.base import Base
from app.models import user, subscriptions
engine = create_async_engine(
    settings.connection_url, 
    echo=True,
    connect_args={
        "statement_cache_size": 0
    })

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



async def get_db():
    async with async_session() as session:
        yield session