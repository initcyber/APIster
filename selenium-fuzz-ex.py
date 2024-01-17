from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=localhost:8080')
driver = webdriver.Chrome(options=options)
driver.get('https://www.example.com')

# Mozilla or Chrome Developer Tools to intercept HTTP requests, can be obtained the selenium library3. 
# The above is a sample code snippet that uses selenium to intercept HTTP requests.

# This code snippet sets up a proxy server at localhost:8080 and uses it to intercept HTTP requests made by the Chrome browser.