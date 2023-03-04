from src.read_config import read_file
# from db.database import async_db_session
from src.server import run_server
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
    await run_server(config_data['controller_port'], config_data['rest_ip'], config_data['rest_port'])


if __name__ == '__main__':
    asyncio.run(async_main())

