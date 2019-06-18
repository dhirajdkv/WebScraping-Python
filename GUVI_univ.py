from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import re
count = 0
# FUNCTION FOR REMOVING HTML TAGS AND PRINTING OP
def remove_html_tags(text):
    """Remove html tags from a string"""
    global count
    clean = re.compile('<.*?>')
    var = re.sub(clean, '', str(item))
    # FOR ADDING NUMBERS ON SAME LINE
    if count < 2:
        print(var,end='   ')
        count+=1
    if count > 1:
        count = 0
        print("\n")
    if var.isnumeric()==False:
        college_names.append(var)
        
college_names = []
flag=0
count = 0
headers = {'user-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
qpage = "https://www.guvi.in/automation/collegeID.php"
req = Request(url=qpage,headers=headers)
html = urlopen(req).read()
reqsoup = soup(html, "html.parser")
div = reqsoup.findAll("td")
for item in div:
    remove_html_tags(item)

#Activate the below mentioned code if you want to give input as college code and get college name:    
'''
college_names.insert(0,' ')
while(flag==0):
    college_code = input("Enter college code or enter exit:")
    if college_code == "exit":
        flag=1
    elif int(college_code) <= len(college_names):
        print(college_names[int(college_code)-1])
        flag=0
    else:
        print("Incorrect college code")
        flag=0
'''
