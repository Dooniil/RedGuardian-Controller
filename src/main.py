from src.read_config import read_file
# from db.database import async_db_session
from src.services.active_conn import active_conn
from src.server import run_server
from src.services.scanner_service import periodic_check_conn
import asyncio
import os


config_data = dict()


async def async_main() -> None:
    tasks_read_configs: list[asyncio.Task] = [
        asyncio.create_task(read_file(f'{os.sep.join([os.getcwd(), "controller_config.cfg"])}')),
        asyncio.create_task(read_file(f'{os.sep.join([os.getcwd(), "rest_config.cfg"])}')),
        asyncio.create_task(read_file(f'{os.sep.join([os.getcwd(), "db_config.cfg"])}'))
    ]

    for item in await asyncio.gather(*tasks_read_configs):
        config_data.update(item)

    # await async_db_session.init(config_data)
    periodic_checking_task = asyncio.create_task(periodic_check_conn(active_conn))
    await asyncio.gather(run_server(config_data['controller_port'], active_conn), periodic_checking_task)


if __name__ == '__main__':
    asyncio.run(async_main())

