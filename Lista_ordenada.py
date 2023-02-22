def ordenada(lista):
    fim = len(lista)

    for i in range(fim - 1):
        # Inicialmente, o menor elemento já visto é o i-ésimo
        posicao_do_minimo = i

        for j in range(i+1, fim):
            if lista[posicao_do_minimo] > lista[j]:
                return False
    return True
