import asyncio

from db.database import async_db_session
from db.models import Family, Platform, Vulnerability


async def create_family():
    await Family.create(name='Windows')
    family = await Family.get(1)
    return family.id


async def init_app():
    await async_db_session.init()
    # await async_db_session.create_all()


async def async_main():
    await init_app()

if __name__ == '__main__':
    asyncio.run(async_main())
