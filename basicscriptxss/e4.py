import requests

url = "https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/"
response = requests.get(url)
print(response.text)