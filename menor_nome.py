def menor_nome(nomes):
    pos_nome1 = 0
    pos_nome2 = 1
    nome_menor = ""
    for i in range(len(nomes)):
        #correr lista de nomes
        nomes[i] = nomes[i].strip()
        nomes[i] = nomes[i].capitalize()
        j = 0
    if len(nomes) == 1:
        return nomes[0]
    else:
        if len(nomes) == 0:
            return ""
        else:
            while pos_nome2 < (len(nomes)):
                if len(nomes[pos_nome1]) <= len(nomes[pos_nome2]):
                    nome_menor = nomes[pos_nome1]
                    pos_nome2 = pos_nome2 + 1
                else:
                    nome_menor = nomes[pos_nome2]
                    pos_nome1 = pos_nome2
                    pos_nome2 = pos_nome2 + 1
            return nome_menor
