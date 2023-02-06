from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = "postgresql+asyncpg://rg_user:Password12-@localhost:5432/RedGuardian"
Base = declarative_base()


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        self._engine = create_async_engine(DATABASE_URL, echo=True)
        self._session = sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession)()


async_db_session = AsyncDatabaseSession()
