import webbrowser
import requests
import urllib.request
from bs4 import BeautifulSoup
import bs4
import time
diretorio_principal='https://conell.com.br/FTP%20CONEL/ALEX/FOTOS%20FUNCION%C3%81RIOS%20CONEL/'
#Testar conexão do diretorio e capturar tags
code_ok=200
code_forbi=403
code_not=404
requisicao=requests.get(diretorio_principal)
if requisicao.status_code==200:
    print('Diretório Foi encontrado!')
    time.sleep(2)
elif requisicao.status_code==403:
    print('Diretório não pode ser acessado!')
    time.sleep(2)
elif requisicao.status_code==404:
    print('Diretório não encontrado!')
    time.sleep(2)
#Encontrar os Links
def encontrar_diretorios(url):
 html = requests.get(url)
 soup=bs4.BeautifulSoup(html.content,'html.parser')
 for a in soup.find_all('a', href=True):
     print ("Found the URL:", a['href'])
     time.sleep(2)
     diretorio_combinado=diretorio_principal+a['href']
     webbrowser.open(diretorio_combinado)
     
encontrar_diretorios(diretorio_principal)








    

