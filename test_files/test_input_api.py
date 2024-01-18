import re
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Path to your ChromeDriver executable
chrome_path = "/usr/local/bin/chromedriver-linux64/chromedriver"

# Initialize ChromeDriver
driver = webdriver.Chrome(
    service=ChromeService(executable_path=chrome_path), options=chrome_options
)

# Ask the user for the base URL
base_url = input("Enter the base URL: ") + ":"

# Ask the user for the range of ports to scan
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Set the implicit wait time to 1 second
driver.implicitly_wait(1)

# Loop through port numbers from start_port to end_port
for port in range(start_port, end_port):
    # Navigate to the webpage
    url = base_url + str(port)
    try:
        driver.get(url)
    except WebDriverException:
        # print(f"Could not connect to {url}")
        continue

    # Capture network requests
    network_requests = driver.execute_script("return window.performance.getEntries();")

    # Filter for API endpoints
    api_endpoints = []
    for request in network_requests:
        if re.search(r"API", request["name"]) or re.search(r"api", request["name"]):
            api_endpoints.append(request["name"])

    # Print the captured API endpoints
    for endpoint in api_endpoints:
        print(endpoint)

# Close the browser
driver.quit()
