def nome_mais_curto (lista_de_nomes):
    pos_nome1 = 0
    pos_nome2 = 1
    nome_menor = ""
    for i in range(len(lista_de_nomes)):
        #correr lista de nomes
        lista_de_nomes[i] = lista_de_nomes[i].strip()
        #lista_de_nomes[i] = lista_de_nomes[i].capitalize()
        j = 0
    if len(lista_de_nomes) == 1:
        return lista_de_nomes[0]
    else:
        if len(lista_de_nomes) == 0:
            return ""
        else:
            while pos_nome2 < (len(lista_de_nomes)):
                if len(lista_de_nomes[pos_nome1]) <= len(lista_de_nomes[pos_nome2]):
                    nome_menor = lista_de_nomes[pos_nome1]
                    pos_nome2 = pos_nome2 + 1
                else:
                    nome_menor = lista_de_nomes[pos_nome2]
                    pos_nome1 = pos_nome2
                    pos_nome2 = pos_nome2 + 1
            return nome_menor

            
            
def test_nome_mais_curto ():
    lista_a = [" Ana    ", "    NuNo    ", "  Andre   "]
    lista_b = ["    NuNo    ", "  Andre   "," Ana    "]
    lista_c = [ "  Andre   ", " Ana    ", "    NuNo    "]
    lista_d = []
    nome_a = nome_mais_curto (lista_a)
    nome_b = nome_mais_curto (lista_b)
    nome_c = nome_mais_curto (lista_c)
    nome_d = nome_mais_curto (lista_d)
    
    if nome_a == "Ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_a)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_a)

    nome_b = nome_mais_curto (lista_b)
    if nome_b == "Ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_b)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_b)

    nome_c = nome_mais_curto (lista_c)
    if nome_c == "Ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_c)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_c)

    nome_d = nome_mais_curto (lista_d)
    if nome_d == "":
        print("O teste 1 está a funcionar e deu o nome:", nome_d)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_d)
