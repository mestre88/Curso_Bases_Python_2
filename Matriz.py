def cria_matriz_valor(num_linhas, num_colunas, valor):
    '''(int,int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado
    '''
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        # adiciona linha à matriz
        matriz.append(linha)
    return matriz




def cria_matriz_digitada(num_linhas, num_colunas):
    '''(int,int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo utilizador
    '''
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)

    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    matriz = cria_matriz_digitada(lin, col)
    imprime_matriz (matriz)
    return matriz


def imprime_matriz (matriz):
    '''
    Recebe matriz que é uma lista de listas e imprime a matriz da forma matematica
    '''
    for i in range(len(matriz)):
        #Posição das linhas
        j = 0
        for j in range(len(matriz[j])):
            #Posição das colunas
            print(matriz[i][j], end = ' ')
        print()
    
