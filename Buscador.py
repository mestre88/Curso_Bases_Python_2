import random
import time

class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1

    def lista_ordenada(self, n):
        lista = [x for x in range(n)]
        return lista

    def compara(self, n):
        lista1 = self.lista_ordenada(n)
        print("Comparando busca sequencial")
        a = int(input("Digite o numero a procurar: "))
        antes = time.time()
        pos = self.busca_sequencial(lista1, a)
        depois = time.time()
        print("busca sequencial demorou ", depois - antes, " Na posição: ", pos)

        print("\nComparando busca Binaria")
        antes = time.time()
        pos = self.busca_binaria(lista1, a)
        depois = time.time()
        print("busca binaria demorou ", depois - antes, " Na posição: ", pos)
        
