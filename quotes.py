from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import re

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    var = re.sub(clean, '', str(fitem))
    print(var.strip('[]'))

headers = {'user-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
qpage = "https://www.4icu.org/in/indian-universities.htm"
req = Request(url=qpage,headers=headers)
html = urlopen(req).read()
reqsoup = soup(html, "html.parser")
div = reqsoup.findAll("td")
for item in div:
    fitem = item.findAll("a")
    remove_html_tags(fitem)

