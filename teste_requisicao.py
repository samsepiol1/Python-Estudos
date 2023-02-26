import requests
from random import randint
var_numero=randint(0,100)
numero_transformado=str(var_numero)
endereco='http://ead.unirn.edu.br/user/view.php?id='+numero_transformado
print(endereco)
requisicao=requests.get(endereco)
print(requisicao.status_code)
