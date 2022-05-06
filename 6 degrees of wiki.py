from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import random
import datetime
import re
random.seed(datetime.datetime.now())
degrees = int(input("How many degrees of bacon?:"))
current_articules = 0
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

def readTitle(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for title in bs.find('h1', 'firstHeading'): 
        return title

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0 and current_articules < degrees:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    current_articules += 1
    print(current_articules, ": ", newArticle)
    if(current_articules<degrees):
        links = getLinks(newArticle)
print(readTitle(newArticle))