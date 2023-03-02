async def read_file(path_file: str):
    data = {}
    with open(path_file, 'r') as file:
        for line in file:
            key, value = line.split()[0], line.split()[2]
            data[key] = value
    return data
