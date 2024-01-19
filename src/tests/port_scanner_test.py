import socket
import unittest


class TestScanPorts(unittest.TestCase):
    def test_scan_ports(self):
        target = "google.com"
        expected_ports = [80, 443]
        actual_ports = scan_ports(target)
        self.assertEqual(expected_ports, actual_ports)


def scan_ports(target):
    open_ports = []
    for port in range(8686, 8990):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports


if __name__ == "__main__":
    unittest.main()
