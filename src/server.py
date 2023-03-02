from src.read_config import read_file
from src.services.actual_scanners_checker import add_scanner
import os
import json
import asyncio


HOST_IP = '127.0.0.1'
rest_ip = read_file(os.sep.join([os.getcwd(), 'rest_config.cfg'])).get('rest_ip')


async def controller_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr, port = writer.get_extra_info('peername')
    # if addr == rest_ip:
    #     data = await reader.read(1536)
    #     json_request: dict = json.loads(data)
    # else:
    print(f'{addr}:{port}')
        # print(add_scanner(addr, port))


async def run_server(port: int) -> None:
    server = await asyncio.start_server(controller_handler, HOST_IP, port)
    async with server:
        await server.serve_forever()
