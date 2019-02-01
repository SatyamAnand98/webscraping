from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

i=0

my_url = 'https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&N=-1&isNodeId=1'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})
# print(soup.prettify(containers[0]))

filename = "scrape.csv"
f = open(filename, "w")
headers = "sl.no., Product\n"
f.write(headers)

for container in containers:
    i += 1
    product = container.a.img["title"]
    f.write(str(i)+","+product.replace(",","|")+"\n")

f.close()
