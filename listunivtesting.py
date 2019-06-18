from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import re

##FINDING SUBSTRINGS OF UNIVERSITIES LIKE IIT FOR INDIAN INSTITUTE OF TECHNOLOGY!!
def finding_substring(text,realtext):
    letters = [word[0] for word in text]
    let_join = "".join(letters)
    if inp in let_join.lower():
        print(realtext)

##CHECKING IF THE INPUT MATCHES WITH ANY OF UNIVERSITIES        
def finding_item(stext):
    text_split = stext.split()
    if inp in stext.lower():
        print(stext)
    else:
        if "of" in text_split:
            text_split.remove("of")
            finding_substring(text_split,stext)

##BELOW CODE IS FOR REMOVING THE HTML TAGS FROM SCRAPED WEBPAGE!!    
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    var = re.sub(clean, '', str(fitem))
    var_strip = var.strip("[]")
    if var_strip != '':
        f.append(var_strip)
        finding_item(var_strip)
        
## GETTING INPUT AND SCRAPING THE WEBSITE USING SOUP AND REQUESTS   
inp = input("Enter university name or short name ex:IIT")
f=[]
headers = {'user-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
qpage = "https://www.4icu.org/in/indian-universities.htm"
req = Request(url=qpage,headers=headers)
html = urlopen(req).read()
reqsoup = soup(html, "html.parser")
div = reqsoup.findAll("td")
for item in div:
    fitem = item.findAll("a")
    remove_html_tags(fitem)




