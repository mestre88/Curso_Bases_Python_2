def menor_string_ordem_lexicográfica (lista_de_strigs):
    pos_string_a = 0
    pos_string_b = 1
    string = ""    
    for i in range(len(lista_de_strigs)):
        lista_de_strigs[i] = lista_de_strigs[i].strip()
        lista_de_strigs[i] = lista_de_strigs[i].lower()
    if len(lista_de_strigs) == 0:
        return ""
    else:
        if len(lista_de_strigs) == 1:
            return lista_de_strigs[0]
        else:
            while pos_string_b < len(lista_de_strigs):
                if lista_de_strigs[pos_string_a] <= lista_de_strigs[pos_string_b]:
                    string = lista_de_strigs[pos_string_a]
                else:
                    string = lista_de_strigs[pos_string_b]
                    pos_string_a = pos_string_b
                    
                pos_string_b = pos_string_b + 1
            return string



def test_nome_mais_curto ():
    lista_a = [" Ana    ", "    NuNo    ", "  Andre   "]
    lista_b = ["    NuNo    ", "  Andre   "," Ana    "]
    lista_c = [ "  Andre   ", " Ana    ", "    NuNo    "]
    lista_d = []
    nome_a = menor_string_ordem_lexicográfica(lista_a)
    nome_b = menor_string_ordem_lexicográfica(lista_b)
    nome_c = menor_string_ordem_lexicográfica(lista_c)
    nome_d = menor_string_ordem_lexicográfica(lista_d)
    
    if nome_a == "ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_a)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_a)

    if nome_b == "ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_b)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_b)

    if nome_c == "ana":
        print("O teste 1 está a funcionar e deu o nome:", nome_c)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_c)

    if nome_d == "":
        print("O teste 1 está a funcionar e deu o nome:", nome_d)
    else:
        print("O teste 1 Não Funcionou!! e deu o nome:", nome_d)
