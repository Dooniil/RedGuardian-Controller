from sqlalchemy.orm import declarative_base

from src.startup_loading import addresses, initial

if not addresses:
    initial()

DATABASE_URL = f"postgresql+asyncpg://{addresses.get('db_user')}:{addresses.get('db_pass')}@{addresses.get('db_host')}" \
               f":{addresses.get('db_port')}/{addresses.get('db_name')}"
Base = declarative_base()
