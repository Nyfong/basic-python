import requests
from bs4 import BeautifulSoup
url = "https://www.passiton.com/inspirational-quotes"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = []
quote_boxes = soup.find_all('div', class_='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top')
for box in quote_boxes:
    quote_text = box.img['alt'].split(" #")
    quote = {
        'theme': box.h5.text.strip(),
        'image_url': box.img['src'],
        'lines': quote_text[0],
        'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
    }
    quotes.append(quote)
# Display extracted quotes
for q in quotes[:5]:  # print only first 5 for brevity
    print(q)