def main ():
    fox = cao("Fox", 2, "Dourada", 11)
    joy = cao("Joy", 1, "Castanha", 6)

    fox.anda()
    joy.anda()
    joy.para()
    fox.para()


class cao:
    def __init__ (self, nome, idade, cor, peso):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.peso = peso
        self.movimento = False

    def anda(self):
        self.movimento = True
        print ("A %s , com idada de %d ano e cor %s está a andar!"%(self.nome, self.idade, self.cor))

    def para(self):
        self.movimento = False
        print ("A %s , com idada de %d ano e cor %s está parada!"%(self.nome, self.idade, self.cor))
        
main()
