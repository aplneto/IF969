class _No():
    def __init__(self, chave, valor, esquerda = None, direita = None):
        self.chave = chave
        self.valor = valor
        self.e = esquerda
        self.d = direita
    
    def __str__(self):
        return '{}: {}'.format(repr(chave), repr(valor))
    
    def __repr__(self):
        return self.__str__()

class _NoD():
    def __init__(self, chavemin, chavemax, valormin, valormax, esquerda = None,
                 meio = None, direita = None):
        self.chavemin = chavemin
        self.chavemax = chavemax
        self.valormin = valormin
        self.valormax = valormax
        self.e = esquerda
        self.m = meio
        self.d = direita
    
    def __str__(self):
        return "{}: {}, {}: {}".format(self.chavemin, self.valormin,
                                       self.chavemax, self.valormax)
    
    def __repr__(self):
        return self.__str__()
    
class Arvore():
    def __init__(self, iteravel = None):
        self.raiz = None
        for chave, valor in iteravel:
            self.inserir(chave, valor)
    
    def inserir(self, chave, valor):
        self.__inserir(chave, valor, self.raiz)
    
    def __inserir(self, chave, valor, no):
        pass