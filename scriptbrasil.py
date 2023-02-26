import bs4 as bs
import urllib.request
import re
sauce=urllib.request.urlopen('https://www.placardefutebol.com.br/')
soup=bs.BeautifulSoup(sauce,'lxml')
body=soup.body
for div in soup.find_all(re.compile(r'div',class_='w-25 p-2 team-name'|class_='w-25 p-1 status text-center')):
    print(' {}x'.format(div.text))
                        
                        

