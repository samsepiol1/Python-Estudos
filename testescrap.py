import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver=webdriver.Chrome('C:/Users/Deus/Downloads/chromedriver.exe')
driver.get('https://www.tecmundo.com.br/')
html=driver.page_source
driver.quit()
soup=BeautifulSoup(html,'lxml')
teste=soup.FindElementByDataBind("title").Text()
print(teste)
#harsh=soup.find('a',{"href": "Url", "title": "Title"}).text()
#print(harsh)
