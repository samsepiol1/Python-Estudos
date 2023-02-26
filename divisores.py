def divisores(num):
    for i in range (1, num//2+1):
        if num % i == 0:
            yield i
    yield num
num = 17231287
print(list(divisores(num)))
