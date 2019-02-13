from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://itarena.ua/speakers/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"col-xs-6 col-sm-4 col-md-3 speaker-wrap"})
desig_containers = page_soup.findAll("div", {"class":"about"})
name_containers = page_soup.findAll("div",{"class":"name"})
social = page_soup.findAll("div", {"class":"speaker-social-wrap"})

c = 0
for container in containers:
    c += 1

filename = "scrape.csv"
f = open(filename, "w")
headers = "Event Name, Name, Image Link, Designation, Company, Short Bio, Country, Linkedin\n"
f.write(headers)

event_name = "IT Arena"

for i in range(c):
    '''country'''
    country = containers[i].div["data-country"]

    '''image link'''
    image = containers[i].div.div.a["href"]

    '''name'''
    # print(soup.prettify(name_containers[0]))
    name = name_containers[i].a.text

    '''designation'''
    desig = desig_containers[i].div.text.lstrip()

    '''linkedin'''
    ldin = social[i].a["href"]

    '''company'''
    comp = desig_containers[i].a.text.lstrip()

    '''bio'''
    lnk = container.div.div.a["href"]
    uClient2 = uReq(lnk)
    page_html2 = uClient2.read()
    uClient2.close()
    page_soup2 = soup(page_html2, "html.parser")
    containers2 = page_soup2.find("div", {"class":"speaker-about"})
    short_bio = containers2.text

    f.write(event_name+','+name+','+image+','+'.'.join(desig.split(','))+','+'.'.join(comp.split(','))+','+'.'.join(short_bio.split(','))+','+country+','+ldn+'\n')
    # name = containers[0].findAll("div",{"class":"name"})
    # print(name)

    # print(page_soup)
    # print(soup.prettify(containers[0]))
    # containers = page_soup.findAll("div", {"class":"_3liAhj _1R0K0g"})

