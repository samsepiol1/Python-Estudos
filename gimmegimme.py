import bs4 as bs
from bs4 import BeautifulSoup
import requests
import re
sauce=requests.get('https://news.ycombinator.com/')
soup=BeautifulSoup(sauce.text,'lxml')
for tag in soup.find_all('title'):
    print()
for a in soup.find_all('a',class_="storylink"):
    teste_a=a.text
    print(teste_a)
    name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
    names = name_pattern.findall(teste_a)
    print(names)
nome=tag.text
