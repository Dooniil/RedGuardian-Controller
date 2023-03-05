import asyncio


WINDOWS_CHECK_VERSION_CMD = ['$PSVersionTable.BuildVersion.Major', '$PSVersionTable.BuildVersion.Minor',
                             '$PSVersionTable.BuildVersion.Build', '$PSVersionTable.BuildVersion.Revision']
LINUX_CHECK_VERSION_CMD = ['lsb_release -i', 'lsb_release -r', 'lsb_release -c']


# add check x64
def check_version(transport_type: int, credential_type: int):
    match (transport_type, credential_type):
        case (0, 0):  # Windows & WinRM
            major, minor, build, revision = (1, 1, 1, 1)  # send cmd
        case (1, 0):  # Linux & SSH
            name, version, code_name = (1, 1, 1)  # send cmd


async def check_conn(active_conn, conn_data, key) -> None:
    try:
        r, w = asyncio.open_connection(conn_data['name_scanner'][0], conn_data['name_scanner'][1])
        w.close()
        await w.wait_closed()
    except Exception:
        active_conn.pop(key)


async def periodic_check_conn(active_conn: dict):
    while True:
        print(active_conn)
        if active_conn:
            tasks_check_conn = [asyncio.create_task(check_conn(active_conn, conn_data, key))
                                for key, conn_data in active_conn.items()]

            done, pending = await asyncio.wait(tasks_check_conn)
        await asyncio.sleep(10)
