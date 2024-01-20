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

        # Check if a POST request works
        try:
            post_button = driver.find_element_by_id("post_button")
            post_button.click()
            time.sleep(5)
            response = driver.page_source
            if "Success!" in response:
                print(f"POST request works on {url}")
            else:
                print(f"POST request does not work on {url}")
        except:
            print(f"POST request does not work on {url}")

        # Check if a GET request works
        try:
            get_button = driver.find_element_by_id("get_button")
            get_button.click()
            time.sleep(5)
            response = driver.page_source
            if "Success!" in response:
                print(f"GET request works on {url}")
            else:
                print(f"GET request does not work on {url}")
        except:
            print(f"GET request does not work on {url}")

    # Close the browser
    driver.quit()


### Can run this alone using python api_scanner.py <ip address> <port 1> <port 2> <port 3> <port 4> <port 5> etc...
if __name__ == "__main__":
    ip_address = sys.argv[1]
    ports = sys.argv[2:]
    scan_api(ip_address, ports)
