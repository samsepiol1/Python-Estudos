horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas:'))

salario_extra = 0

if (horas_trabalhadas>=30 and horas_trabalhadas<=40):

    horario_extra = 40-horas_trabalhadas
    salario_extra = horario_extra * 150
    salario_total = 800+salario_extra
    print(salario_total)
    




