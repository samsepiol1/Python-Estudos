#Logica do Script

import json
import requests
r = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')

requisicao_dados =r.json()


def valor_bitcoin():
    return print("O preco do Bitcoin agora e: R$ {:.2f}".format(float(requisicao_dados['ticker']['last'])))
valor_bitcoin()


