from seleniumwire import webdriver
from bs4 import BeautifulSoup
import time

# Start browser with selenium-wire
options = {}
driver = webdriver.Chrome(seleniumwire_options=options)

# Target site (example form page)
url = "https://uc.edu.kh/"
driver.get(url)

time.sleep(2)  # wait for page load

# Parse page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find CSRF token in hidden input
csrf_token = None
token_input = soup.find("input", {"name": "csrf_token"})
if token_input:
    csrf_token = token_input.get("value")

print("CSRF Token (from HTML form):", csrf_token)

# Check requests made (headers may also contain CSRF)
for request in driver.requests:
    if request.response:
        if "csrf" in str(request.headers).lower():
            print("CSRF in headers:", request.headers)

driver.quit()
