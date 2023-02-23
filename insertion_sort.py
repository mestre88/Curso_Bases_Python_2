def insertion_sort (lista):
    tamanho = len(lista)

    for i in range(1, tamanho):
        for j in range(i):
            if lista[j] > lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
    return lista
