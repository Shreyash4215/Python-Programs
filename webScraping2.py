import requests
import bs4 

res = request.get("https://en.wikipedia.org/wiki/Nature")

res.text
soup = bs4.Beautifulsoup(res.text,'lxml')
soup.select(".author")

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)

soup = bs4.Beautifulsoup(res.text,'xml')
soup.select('.tag-item')
for item in soup.select(".tag-item"):
    print(item.text)
   

