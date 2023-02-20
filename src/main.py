from src.server import ThreadedTCPServer, ControllerTCPHandler, CONTROLLER_HOST, CONTROLLER_PORT


# async def create_family():
#     await Family.create(name='Windows')
#     family = await Family.get(1)
#     return family.id


# async def init_app():
    # await async_db_session.init()
    # await async_db_session.create_all()


async def async_main():
    # await init_app()
    pass

if __name__ == '__main__':
    with ThreadedTCPServer((CONTROLLER_HOST, int(CONTROLLER_PORT)), ControllerTCPHandler) as server:
        server.serve_forever()
