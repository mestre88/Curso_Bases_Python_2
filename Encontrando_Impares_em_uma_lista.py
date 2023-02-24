def  encontra_impares(lista):
    if len(lista) == 1:
        if lista[len(lista)-1] % 2 != 0:
            return lista
    if len(lista) < 1:
        return lista
    else:
        while len(lista) > 0:
            lista_impar = []
            lista_corta = []
            if lista[len(lista)-1] % 2 != 0:
                lista_impar.append(lista[len(lista)-1])
            lista_corta = lista[:len(lista)-1]
            return lista_impar + encontra_impares(lista_corta[:len(lista)])
            
