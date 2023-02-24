def soma_lista(lista):
    if len(lista) <= 1:
        return lista[len(lista)-1]
    else:
        valor = lista[len(lista)-1]
        nova_lista = lista[:len(lista)-1]
        return valor + soma_lista(nova_lista)

