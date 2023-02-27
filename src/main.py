from src.config_loading import initial
from src.server import run_server
import asyncio
import os


async def async_main():
    controller_port: int = initial(os.sep.join([os.getcwd(), 'controller_config.cfg'])).get('controller_port')

    tasks = [run_server(controller_port)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(async_main())

