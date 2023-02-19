import Matriz

def soma_matrizes (A, B):
    num_lin = len(A)
    num_col = len(A[0])
    num_lin_b = len(B)
    num_col_b = len(B[0])
    assert num_lin == num_lin_b and num_col == num_col_b
    C = Matriz.cria_matriz_valor(num_lin, num_col, 0)

    for lin in range(num_lin): # percorre as linhas da matriz
        for col in range(num_col): # percorre as colunas da matriz
            C[lin][col] = A[lin][col] + B[lin][col]
    return C





def multiplica_matrizes (A, B):
    num_lin_a = len(A)
    num_col_a = len(A[0])
    num_lin_b = len(B)
    num_col_b = len(B[0])
    assert num_col_a == num_lin_b
    
    C = []
    linhas = []

    for lin_a in range(num_lin_a): # percorre as linhas da matriz A
        for col_b in range(num_col_b): # percorre as colunas da matriz B
            calculo = 0
            for col_a in range(num_col_a): # percorre as linhas da matriz B
                calculo = calculo + ((A[lin_a][col_a]) * (B[col_a][col_b]))
            linhas.append(calculo)
        C.append(linhas)
        linhas = []
    return C





if __name__ == '__main__':
    #A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    #print(soma_matrizes(A, B))
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(multiplica_matrizes(A, B))
