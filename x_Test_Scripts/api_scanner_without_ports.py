import re
import time

from selenium import webdriver
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

# Navigate to the webpage/url
url = "http://172.16.10.10:8989"
driver.get(url)

# Allow some time for dynamic content to load
time.sleep(5)

# Capture network requests
network_requests = driver.execute_script("return window.performance.getEntries();")

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

# THIS WORKS! It only does one website:port however
