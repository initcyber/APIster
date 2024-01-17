#!/usr/bin/env python3

import argparse

RED = "\033[91m"
ENDC = "\033[0m"


def display_banner():
    banner = """

░░      ░░       ░░        ░        ░  ░░░░  ░        ░        ░        ░
▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒
▓  ▓▓▓▓  ▓       ▓▓▓▓▓  ▓▓▓▓      ▓▓▓  ▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓
█        █  ██████████  ████  ███████  ████  ██  ███████  ███████  ██████
█  ████  █  ███████        █  ████████      ██        █        █        █
                                                                         
"""
    print(RED + banner + ENDC)
    print("Justin Johnson / @initcyber / justin@initcyber.com\n")


if __name__ == "__main__":
    display_banner()
    parser = argparse.ArgumentParser(
        description="API Fuzzz: Scan and discover API's on websites."
    )
