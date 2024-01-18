# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=localhost:8080')
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.initcyber.com')


# Mozilla or Chrome Developer Tools to intercept HTTP requests, can be obtained the selenium library3.
# The above is a sample code snippet that uses selenium to intercept HTTP requests.

# This code snippet sets up a proxy server at localhost:8080 and uses it to intercept HTTP requests made by the Chrome browser.


# install Chrome for testing

# meta_data=$(curl 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
# wget $(echo "$meta_data" | jq -r '.channels.Stable.downloads.chromedriver[0].url')
# unzip chromedriver-linux64.zip
# sudo apt install python3-venv -y
# python3 -m venv .venv
# source .venv/bin/activate

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

# Navigate to the webpage
url = "https://youtube.com"
driver.get(url)

# Allow some time for dynamic content to load
time.sleep(5)

# Capture network requests
network_requests = driver.execute_script("return window.performance.getEntries();")

# Print the captured network requests
for request in network_requests:
    print(request["name"])

# Close the browser
driver.quit()


# wget $(echo "$meta_data" | jq -r '.channels.Stable.downloads.chromedriver[0].url')
#  unzip chromedriver_linux64.zip
#    sudo mv chromedriver /usr/local/bin/

# sudo apt install chromium-chromedriver
