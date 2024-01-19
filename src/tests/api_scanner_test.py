# api_scanner.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from api_scanner import scan_api


class TestScanAPI(unittest.TestCase):
    def test_scan_api(self):
        ip_address = "172.16.10.10"
        ports = ["80", "443", "8686"]
        expected_api_endpoints = [
            "http://172.16.10.10:80/api/endpoint",
            "http://172.16.10.10:443/api/endpoint",
            "http://172.16.10.10:8686/api/endpoint",
        ]
        actual_api_endpoints = scan_api(ip_address, ports)
        self.assertEqual(actual_api_endpoints, expected_api_endpoints)


if __name__ == "__main__":
    unittest.main()
"""

# This unit test is all broken...
