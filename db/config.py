from sqlalchemy.orm import declarative_base
from src.config_loading import initial
import os

db_info: dict = initial(os.sep.join([os.getcwd(), 'db_config.cfg']))

DATABASE_URL = f"postgresql+asyncpg://{db_info.get('db_user')}:{db_info.get('db_pass')}@{db_info.get('db_host')}" \
               f":{db_info.get('db_port')}/{db_info.get('db_name')}"
Base = declarative_base()
