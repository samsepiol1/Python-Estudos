from bs4 import BeautifulSoup
import requests
import time
tempo_execucao=time.time()
pagina=requests.get("http://www.vestibular.ita.br/inscritos/v2019_a.htm")
soup=BeautifulSoup(pagina.content, 'lxml')
table=soup.find("td")
print(pagina.status_code)
print("Tempo de resposta da requisição:{}".format(tempo_execucao))
tabela_em_texto=table.get_text()
print(tabela_em_texto)



