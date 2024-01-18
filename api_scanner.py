import re
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

"""
def scan_api(open_ports, ip_address):
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    # Path to your ChromeDriver executable
    chrome_path = "/usr/local/bin/chromedriver-linux64/chromedriver"

    # Initialize ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_path), options=chrome_options)

    # Define the base URL
    base_url = ip_address

    # Set the implicit wait time to 1 second
    driver.implicitly_wait(1)

    # Loop through port numbers from 1 to 10000
    for port in range(open_ports):
        open_apis = []
        # Navigate to the webpage
        url = base_url + str(port)
        try:
            driver.get(url)
        except WebDriverException:
            #print(f"Could not connect to {url}")
            continue

        # Capture network requests
        network_requests = driver.execute_script("return window.performance.getEntries();")

        # Filter for API endpoints
        api_endpoints = []
        for request in network_requests:
            if re.search(r'API', request['name']) or re.search(r'api', request['name']):
                api_endpoints.append(request['name'])

        # Print the captured API endpoints
        for endpoint in api_endpoints:
            print(endpoint)
            return(open_apis)

    # Close the browser
    driver.quit()
    
"""


def scan_api(open_ports, ip_address):
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

    # Define the base URL
    base_url = ip_address + ":"

    # Set the implicit wait time to 1 second
    driver.implicitly_wait(1)

    # Initialize an empty list to store the captured API endpoints
    open_apis = []

    # Loop through port numbers from 1 to 10000
    for port in range(open_ports):
        # Navigate to the webpage
        url = base_url + str(port)
        try:
            driver.get(url)
        except WebDriverException:
            # print(f"Could not connect to {url}")
            continue

        # Capture network requests
        network_requests = driver.execute_script(
            "return window.performance.getEntries();"
        )

        # Filter for API endpoints
        api_endpoints = []
        for request in network_requests:
            if re.search(r"API", request["name"]) or re.search(r"api", request["name"]):
                api_endpoints.append(request["name"])

        # Append the captured API endpoints to the open_apis list
        open_apis.extend(api_endpoints)

    # Close the browser
    driver.quit()

    # Return the list of captured API endpoints
    return open_apis
