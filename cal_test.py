import calendar
contador=1
soma=0
trans=[]
for c in range(1,5):
    ano=2019
    soma=ano+c
    day_of_the_week=calendar.weekday(soma,2,17)
    day_of_the_week2=calendar.weekheader(3)
    lista_dias={'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}
    dic={}
    lista=[]
    lista.append(day_of_the_week)
    if lista[0]==0:
        print('Segunda')
        print(lista[0])
    elif lista[0]==2:
        print('Quarta')
        print(lista[0])
         
