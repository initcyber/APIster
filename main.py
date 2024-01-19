#!/usr/bin/env python3


"""
DISCLAIMER:

This software is provided 'as is', without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

This tool is intended to be used for legal purposes only, and the user assumes all responsibility for its use. You must ensure that your use of this tool complies with all local, state, and federal laws and regulations. Any use of this tool for unauthorized activities is strictly prohibited.
"""

import api_scanner
import port_scanner

open_ports = []

RED = "\033[91m"
ENDC = "\033[0m"

# Variables
ports_found = []  # list for Found Ports after using scan_port / port_scanner.py


def display_banner():
    banner = """

    ___    ____  ____     __           
   /   |  / __ \/  _/____/ /____  _____
  / /| | / /_/ // // ___/ __/ _ \/ ___/
 / ___ |/ ____// /(__  ) /_/  __/ /    
/_/  |_/_/   /___/____/\__/\___/_/     
                                       

                                                                        
"""
    print(RED + banner + ENDC)
    print("Justin Johnson / justin@initcyber.com / https://www.github.com/initcyber\n")
    print(
        "Use this software at your own risk, if you get sent to Kaz-BAN-istan, or worse, that's on you..."
    )


def portScanBreakout():
    ip_address = input("Enter IP address: ")
    print(f"This will take a while, we are scanning {ip_address} from ports 1 to 10000")
    # Port Scanning via port_scanner.py
    open_ports = []
    open_ports = port_scanner.scan_ports(ip_address)
    if open_ports:
        print("The following ports are open:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")
    return ip_address, open_ports


def apiScanBreakout_openportselectionTrue(ip_address, open_ports):
    # Port Scanning via api_scanner.py - Imports "port" from port_scanner.py to scan for open API's against those ports...
    print("It's time to use these ports on api_scanner.py")
    open_apis = api_scanner.scan_api(ip_address, open_ports)
    if open_apis:
        print("The following APIs are open:")
        for api in open_apis:
            print(f"API {api} is available")
    else:
        print("No open APIs found")


def apiScanBreakout_default():
    # Port Scanning via api_scanner.py - Imports "port" from port_scanner.py to scan for open API's against those ports...
    print("Bypassing Port Scanning...")
    ip_address = input("Enter IP address: ")
    open_ports = input(
        "Enter the open ports you want to scan for API's, type 'done' when finished :"
    )
    # convert open_ports to list
    open_ports = open_ports.split(",")
    open_ports = [int(port) for port in open_ports]

    # pass open_ports list to api_scanner.py
    open_apis = api_scanner.scan_api(ip_address, open_ports)
    if open_apis:
        print("The following APIs are open:")
        for api in open_apis:
            print(f"API {api} is available")
    else:
        print("No open APIs found")


def main():
    openportselection = input("Do you want to scan for open ports? (y/n): ")
    # Convert openportselection to string
    if openportselection.lower() == "y":
        ip_address, open_ports = portScanBreakout()
        apiScanBreakout_openportselectionTrue(ip_address, open_ports)
    else:
        apiScanBreakout_default()


if __name__ == "__main__":
    display_banner()
    main()

# Need to refactor..
