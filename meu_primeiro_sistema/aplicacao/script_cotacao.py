#Logica do Script

import json
import requests
r = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')

requisicao_dados =r.json()
bitcoin = float(requisicao_dados['ticker']['last'])


def valor_bitcoin():
    return "O preco do Bitcoin agora é: R$ {:.2f}".format(float(requisicao_dados['ticker']['last']))
valor_bitcoin()
