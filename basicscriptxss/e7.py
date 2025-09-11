from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>My Site</title></head>
  <body>
    <h1>Welcome</h1>
    <p class="desc">This is a test</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.text)   # 👉 "My Site"
print(soup.h1)      # 👉 "Welcome"
print(soup.find('p').text)  # 👉 "This is a test"
