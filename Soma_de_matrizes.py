def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        soma_linhas = []
        calc_soma = 0
        for i in range(len(m1)):
            j = 0
            soma_colunas = []
            for j in range(len(m1[j])):
                calc_soma = m1[i][j] + m2[i][j]
                soma_colunas.append(calc_soma)
            soma_linhas.append(soma_colunas)
        return soma_linhas
