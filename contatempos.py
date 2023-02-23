import random
import time
import Ordenacao

class ContaTempos:
    def lista_aleatoria(self,n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista


    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = Ordenacao.Ordenador()
        
        print("comparando com listas aleatorias")
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        o.insertion_sort(lista3)
        depois = time.time()
        print("Insertion sort demorou ", depois - antes)

        

        print("\ncomparando com listas quase ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes)

        antes = time.time()
        o.insertion_sort(lista3)
        depois = time.time()
        print("Insertion sort demorou ", depois - antes)
        
