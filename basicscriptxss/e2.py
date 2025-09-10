import requests  # For HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML responses

# Define the target URL (use your local test server, e.g., http://localhost/vulnerable-form)
url = 'http://test-site.com/submit-form'

# Sample XSS payload (for testing only)
payload = {'input_field': '<script>alert("Simulated XSS")</script>'}

# Send the request
response = requests.post(url, data=payload)

# Parse and check response
soup = BeautifulSoup(response.text, 'html.parser')
if 'alert("Simulated XSS")' in str(soup):  # Naive check; real verification might involve Selenium for JS execution
    print("Potential XSS vulnerability detected.")
else:
    print("No obvious execution.")

# Note: For DOM-based, you might need browser automation like Selenium to simulate user interaction.