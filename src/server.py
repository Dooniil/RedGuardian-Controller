import json
import asyncio


HOST_IP = '127.0.0.1'

rest_conn = []
active_conn = dict()


async def controller_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr, port = writer.get_extra_info('peername')
    msg = await reader.read(1536)
    data = json.loads(msg)
    if addr == rest_conn[0] and port == rest_conn[1]:
        print('Rest connected')
        if data['name_scanner'] in active_conn.keys():
            r, w = asyncio.open_connection(active_conn['name_scanner'][0], active_conn['name_scanner'][1])
            w.write()
            await w.drain(msg)
    else:
        if data['cmd'] == b'connecting':
            if data['name_scanner'] in active_conn.keys():
                print('Such an ID has loaded earlier')
            else:
                active_conn[data['name_scanner']] = (addr, port)

        elif data['cmd'] == b'request':
            pass

        elif data['cmd'] == b'closing':
            active_conn.pop('data[\'name_scanner\']')


async def run_server(port: int, rest_ip: str, rest_port: str) -> None:
    rest_conn.append(rest_ip)
    rest_conn.append(rest_port)

    server = await asyncio.start_server(controller_handler, HOST_IP, port)
    async with server:
        await server.serve_forever()
