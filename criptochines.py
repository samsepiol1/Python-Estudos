#Algoritmo Para Criptografia Criado por uma menina de 12 anos

def esconde(msg):
	s=''
	for c in msg:s+=chr(ord(c)+3000)
	return s
def mostra(msg):
	s=''
	for c in msg: s+=chr(ord(c)-3000)
	return s
