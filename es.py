def selection_sort(lista):
    n = len(lista)

    for j in range(n-1):
        min_index = j

        for i in range(j,n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    return lista
lista = [1,2,4,7,8,9,15,14]
print(selection_sort(lista))
            
    
    
