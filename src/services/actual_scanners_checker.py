actual_scanners = []


def add_scanner(addr, port):
    if (addr, port) not in actual_scanners:
        actual_scanners.append((addr, port))
        return True
    return False
