import requests

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

r = requests.get('http://httpbin.org/headers',headers=headers)
print(r.json())

