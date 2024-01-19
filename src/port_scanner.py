import socket


def scan_ports(target):
    open_ports = []
    for port in range(1, 10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports


# I believe this is refactored enough... Could be wrong
