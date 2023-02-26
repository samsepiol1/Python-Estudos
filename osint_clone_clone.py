import webbrowser
import urllib.request
from bs4 import BeautifulSoup
url_completa='https://br.informacaoes-numero.com/numero/'
numero_de_telefone=input('Insira aqui o seu número de telefone:')
url_de_pesquisa=url_completa+numero_de_telefone
decisao=input('Deseja Abrir no navegador? S/N?').upper()
if decisao=='S':
    url_de_pesquisa=url_completa+numero_de_telefone
    webbrowser.open(url_de_pesquisa)
else:
    page=urllib.request.urlopen(url_de_pesquisa)
    soup=BeautifulSoup(page,'lxml')
    for strong_tag in soup.find_all('strong'):
        print(strong_tag.text)

    





