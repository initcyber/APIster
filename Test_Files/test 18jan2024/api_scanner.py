import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


def scan_api(ip_address, ports):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument(
        "--headless"
    )  # Run Chrome in headless mode (without GUI)

    # Path to your ChromeDriver executable
    chrome_path = "/usr/local/bin/chromedriver-linux64/chromedriver"

    # Initialize ChromeDriver
    driver = webdriver.Chrome(
        service=ChromeService(executable_path=chrome_path), options=chrome_options
    )

    for port in ports:
        # Navigate to the webpage
        url = f"http://{ip_address}:{port}"
        driver.get(url)

        # Allow some time for dynamic content to load
        time.sleep(5)

        # Capture network requests
        network_requests = driver.execute_script(
            "return window.performance.getEntries();"
        )

        # Filter for API endpoints
        api_endpoints = []
        for request in network_requests:
            if re.search(r"API", request["name"]) or re.search(
                r"api", request["name"]
            ):  # and request['name'].startswith(url):
                api_endpoints.append(request["name"])

        # Print the captured API endpoints
        for endpoint in api_endpoints:
            print(endpoint)

    # Close the browser
    driver.quit()

    return api_endpoints


### Can run this alone using python api_scanner.py <ip address> <port 1> <port 2> <port 3> <port 4> <port 5> etc...
if __name__ == "__main__":
    ip_address = sys.argv[1]
    ports = sys.argv[2:]
    scan_api(ip_address, ports)
