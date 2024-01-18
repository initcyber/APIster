#!/usr/bin/env python3

import argparse

import api_scanner

# import test4
import port_scanner

open_ports = []

RED = "\033[91m"
ENDC = "\033[0m"

# Variables
ports_found = []  # list for Found Ports after using scan_port / port_scanner.py


def display_banner():
    banner = """

░░      ░░       ░░        ░        ░  ░░░░  ░        ░        ░        ░
▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒
▓  ▓▓▓▓  ▓       ▓▓▓▓▓  ▓▓▓▓      ▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓
█        █  ██████████  ████  ███████  ████  ██  ███████  ███████  ██████
█  ████  █  ███████        █  ████████      ██        █        █        █
                                                                        
"""
    print(RED + banner + ENDC)
    print("Justin Johnson / justin@initcyber.com / https://www.github.com/initcyber\n")
    print(
        "Use this software at your own risk, if you get sent to Kaz-BAN-istan, or worse, thats on you..."
    )


"""
def main():
    ip_address = input("Enter IP address: ")
    print(f"This will take a while, we are scanning {ip_address} from ports 1 to 10000")
    #Port Scanning via port_scanner.py
    open_ports = port_scanner.scan_ports(ip_address)
    if open_ports:
        print("The following ports are open:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")
    
    #Port Scanning via api_scanner.py - Imports "port" from port_scanner.py to scan for open API's against those ports...
    print("It's time to use these ports on api_scanner.py")
    open_apis = api_scanner.scan_api(port, ip_address)
    if open_apis:
        print("The following ports are open:")
        for apis in open_apis:
            print(f"API {open_apis} is available")
    else:
        print("No open APIs found")
"""


def main():
    ip_address = input("Enter IP address: ")
    print(f"This will take a while, we are scanning {ip_address} from ports 1 to 10000")
    # Port Scanning via port_scanner.py
    open_ports = port_scanner.scan_ports(ip_address)
    if open_ports:
        print("The following ports are open:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")

    # Port Scanning via api_scanner.py - Imports "port" from port_scanner.py to scan for open API's against those ports...
    print("It's time to use these ports on api_scanner.py")
    open_apis = api_scanner.scan_api(len(open_ports), ip_address)
    if open_apis:
        print("The following APIs are open:")
        for api in open_apis:
            print(f"API {api} is available")
    else:
        print("No open APIs found")


if __name__ == "__main__":
    display_banner()
    main()
