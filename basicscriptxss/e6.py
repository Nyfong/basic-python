from bs4 import BeautifulSoup


'''
'html.parser' tells it which parser to use (Python’s built-in HTML parser).

This makes it super easy to navigate and extract data instead of handling messy strings manually.

soup → the variable now holds a "soup object" (parsed HTML tree) that you can search/traverse.
'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify()) # this one will pretty print
 
print(soup.find("head")) # this one will find the first head tag


print(soup.find_all('a')) # this one will find all a tags

# type(tag)

# print(f"type = {type(tag)}")