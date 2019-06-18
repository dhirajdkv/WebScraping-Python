from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
qpage = "https://bluelimelearning.github.io/my-fav-quotes/"
uClient = uReq(qpage)
pagehtml = uClient.read()
uClient.close()
pagesoup = soup(pagehtml, "html.parser")
print(pagesoup)
quotes = pagesoup.findAll("div",{"class":"quotes"})
for quote in quotes:
    favquote = quote.findAll("p",{"class":"aquote"})
    aquote = favquote[0].text.strip()
    favauthors = quote.findAll("p",{"class":"author"})
    author = favauthors[0].text.strip()
    print(aquote)
    print("-"+author)

