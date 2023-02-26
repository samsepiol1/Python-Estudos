import calendar
lista_dias=['Seg','Ter','Qua','Qui','Sex','Sab','Dom']
lista_dias_niver=[]
dic={}
contador=1
soma=0
for c in range(1,5):
    ano=2019
    soma=ano+c
    day_of_the_week=calendar.weekday(soma,2,17)
    lista_dias_niver.append(day_of_the_week)
print(lista_dias)
print(lista_dias_niver)
    
