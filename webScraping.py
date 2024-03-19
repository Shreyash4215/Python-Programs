import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urloprn("https://en.wikipedia.org/wiki/Nature")
htmlFormat = response.read()
htmlFormat

soup = BeautifulSoup(htmlFormat,'html5lib')
text = soup.get_text(strip = true)
tokens = [t for t in text.split()]
print(tokens)

