def getCount(inputStr):
    num_vowels = 0
    Vogais=['A','E','I','O','U']
    for i in range(len(inputStr)):
        if i[inputStr[i]]:
            num_vowels+=1
    return num_vowels
