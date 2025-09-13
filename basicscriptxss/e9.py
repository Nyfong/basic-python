'''
import requests
from bs4 import BeautifulSoup

url = "https://www.rupp.edu.kh/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print("Title:", soup.title.string)   # page title

# find all <input> fields
inputs = soup.find_all("input")
print("\nInput fields:")
for i in inputs:
    print("-", i.get("name"), "| type:", i.get("type"))
'''
#vs

import requests
from bs4 import BeautifulSoup

url = "https://www.rupp.edu.kh/"

# fake browser headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print("Title:", soup.title.string if soup.title else "No title found")

# find all <input> fields
inputs = soup.find_all("input")
print("\nInput fields:")
for i in inputs:
    
    print(f'[+] {i}\n')
