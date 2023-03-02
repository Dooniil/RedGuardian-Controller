from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None
        self._db_url = None

        self._base = declarative_base()

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self, conn_info):
        self._db_url = f"postgresql+asyncpg://{conn_info['db_user']}:{conn_info['db_pass']}@{conn_info['db_host']}" \
                       f":{conn_info['db_port']}/{conn_info['db_name']}"
        self._engine = create_async_engine(self._db_url, echo=True)
        self._session = sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(self._base.metadata.create_all)


async_db_session = AsyncDatabaseSession()
