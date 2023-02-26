addresses = {}


def initial():
    with open('addr.cfg', 'r') as file:
        for line in file:
            key, value = line.split()[0], line.split()[2]
            addresses[key] = value
