import requests

url = input("Enter url: ")

rq = requests.get(url)


print(rq.text)