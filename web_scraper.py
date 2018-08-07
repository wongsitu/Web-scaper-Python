import urllib2
import time
from bs4 import BeautifulSoup
import requests
import re
whitespaces = re.compile('\s+', flags=re.M)
def utf8_to_ascii(s, ws=whitespaces):
    s = s.encode("utf8")
    s = s.decode("ascii", errors="replace")
    s = s.replace(u"\ufffd", " ")
    s = ws.sub(" ", s)
    return s.strip()

abstract = open("C:\Users\Waika Wong\PycharmProjects\untitled11\Abs16", "r+")

for L in range(25081, 25435+1):
    quote_page = "http://www.aapt.org/AbstractSearch/FullAbstract.cfm?KeyID={}".format(L)
    response = requests.get(quote_page)
    html = response.content
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")
    try:
        if "No files found for specified criteria" not in html:
            data=[]
            i=0
            while(i<19):
                name = soup.find_all("font", face="Arial", color="000000", size="2")
                data.append(name[i].contents[0])
                i = i + 1

            list=[]
            for k in data:
                k = utf8_to_ascii(k)
                list.append(k)

            print (list)
            abstract.write(str(list))
            abstract.write("\n")
        time.sleep(5)
    except IndexError:
        continue

"10007 to 25435 range of abstracts"
