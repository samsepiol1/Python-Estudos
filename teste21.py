def droot(num):
    resultado=str(num)
    if len(resultado) == 1:
        return num
    else:
        sum = 0
        for i in resultado:
            sum += int(i)
        num = str(sum)
        return droot(num)
print(droot(345))


