from urllib.parse import urljoin

base_url = "http://example.com/path/to/page.html"
relative_url = "../another/page.html"

absolute_url = urljoin(base_url, relative_url)
print(absolute_url)