def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz

def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")

    
