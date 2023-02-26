msg = [ 'CAD400','Uma Filial...','Solucao','O campo...','','LIB310','A Filial...','Solucao','Foi identificado...','Foi corrigido...','','PAG302','Mudanca...','Solucao','O erro...','O programa...','Programa alterado...']

prfx = ['CAD','PAG','LIB']
dic = {}
key = ''

for m in msg:
    for p in prfx:
        if p in m:
            key = m
            dic[key] = []
            break
    if m != key:
        dic[key].append(m)

print(dic)
