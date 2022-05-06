from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs4 = BeautifulSoup(html.read(), "html.parser")
for link in bs4.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
