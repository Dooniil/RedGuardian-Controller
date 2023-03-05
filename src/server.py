import json
import asyncio
from src.services.active_conn import active_conn


HOST_IP = '127.0.0.1'


async def controller_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr, port = writer.get_extra_info('peername')
    msg = await reader.read(1536)
    data = json.loads(msg)

    if data.get('from') is not None:
        print('Request from rest')
        # if data['name_scanner'] in active_conn.keys():
        #     r, w = asyncio.open_connection(active_conn['name_scanner'][0], active_conn['name_scanner'][1])
        #     w.write()
        #     await w.drain(msg)
        writer.write(b'{status:200}')
        await writer.drain()

    else:
        print('Request from scanner')
        print(active_conn)

        type_req = data.get('cmd')
        match type_req:
            case 'connecting':
                if data['name_scanner'] in active_conn.keys():
                    print('Such an ID has loaded earlier')
                else:
                    active_conn[data['name_scanner']] = (addr, port)
                    print(active_conn)
            case 'request':
                pass
            case 'closing':
                active_conn.pop('data[\'name_scanner\']')
                print(active_conn)


async def run_server(port: int, connections) -> None:
    active_conn.update(connections)

    server = await asyncio.start_server(controller_handler, HOST_IP, port)
    async with server:
        await server.serve_forever()
