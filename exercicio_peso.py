#condições aninhadas
#Determinar Outra soluação e verificar qual a mais adequada

altura = int(input('Digite aqui a sua idade'))

sexo = str(input('Digite seu sexo:F/M'))

k = 1

peso = (altura-100)-(altura-150)/k

if sexo == 'F':
    k = 2
    peso = (altura-100)-(altura-150)/k
    print(peso)
elif sexo == 'M':
    k = 4
    peso = (altura-100)-(altura-150)/k
    print(peso)
