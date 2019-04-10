'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sat Jun  2 11:38:19 2018

Descrição: Código de Classe Auxiliar Polinômios
"""
'''
import numpy

class Polinomio:
    def __init__(self, *coeficientes, dtype = int):
        '''
        Método construtor, recebe como parâmetros os coeficientes dos monômios
        que compõem o polinômio, ignorando monômios de coeficiente 0 com grau
        maior que o primeiro monômio de coeficiente não nulo.
        '''
        # Primeiro precisamos eliminar os zeros a esquerda do Polinômio, caso
        # exista algum.
        i = 0
        for n in coeficientes:
            if n == 0: i += 1   
            else: break
        
        # Depois de encontrarmos a parcela importante dos parâmetros, é
        # necessário criar um vetor para armazenar os coeficientes.
        # Lembrando que, se depois da limpeza do polinômio não existirem mais
        # coeficientes, teremos ainda a constante 0.
        self.coeficientes = numpy.asarray(coeficientes[i:], dtype)\
        if i < len(coeficientes) else numpy.zeros(1, dtype)
        self.grau = len(self.coeficientes)-1
    
    def derivada(self):
        '''
        Método que retorna um polinômio equivalente a derivada do próprio
        objeto.
        '''
        deriv = numpy.ndarray(self.grau, float)
        i = 0
        while i < self.grau:
            # Não é necessário checar a derivada do último coeficiente, visto
            # que é uma constante e a derivada de uma constante é sempre zero.
            deriv[i] = self.coeficientes[i]*(self.grau-i)
            i+=1
        return Polinomio(*deriv)
    
    def newton_raphson(self, x0, tol):
        '''
        Método de Newton-Raphson de estimativa da raiz de um polinômio dados os
        paraâmetros:
        :param x0: valor aproximado da raiz do polinômio
        :param tol: coeficiente de tolerância
        '''
        x = x0
        while abs(self(x)) > tol:
            x -= self(x)/self.derivada()(x)
        return x
    
    def __call__(self, x):
        '''
        Retorna o valor da função de aplicada ao parâmetro x.
        '''
        # Iniciamos o valor da função como 0 e, a medida que vamos calculando o
        # valor de cada monômio, vamos incrementando o resultado ao valor de fx.
        fx = 0
        i = self.grau
        for valor in self.coeficientes:
            if i == 0:  #x^0 = 1
                fx += valor
            elif valor != 0: # Coeficiente zero não afeta o resultado.
                fx += valor*x**i
            i -= 1
        return fx
                
    def __repr__(self):
        '''
        Retorna uma representação válida do objeto.
        '''
        _str = ""
        for c in self.coeficientes:
            if _str: _str += ', '
            _str += str(c)
        return "Polinomio({})".format(_str)
    
    def __str__(self):
        '''
        Retorna uma representação em string do objeto.
        '''
        # O objetivo da formatação da string abaixo é representar o polinomio de
        # forma o mais user friendly possível.
        aux = 0
        fx = ''
        while aux < len(self.coeficientes):
            c = x = e = ''
            mon = '{0}{1}{2}'
            if self.grau > aux: x = 'x'
            if self.grau - aux > 1: e = '^'+str(self.grau-aux)
            if self.coeficientes[aux] < 0: c = str(self.coeficientes[aux])
            elif self.coeficientes[aux] > 0:
                if fx:
                    c += '+'
                if (self.coeficientes[aux] > 1 and x) or (self.grau == aux):
                    c += str(self.coeficientes[aux])
            else:
                c = x = e = ''
            fx += mon.format(c, x, e)
            aux += 1
        return fx
    
    def __getitem__(self, indice):
        '''
        Método que controla a indexação do objeto.
        '''
        # Os polinômios estão ordenados do maior grau para o menor grau, logo
        # o polinomio de maior grau tem índice 0.
        if indice > self.grau:
            raise IndexError (indice)
        # Além disso, um polinômio de grau n é formado por n+1 monômios, pois a
        # constante é um polinômio de grau 0.
        return Polinomio(self.coeficientes[self.grau - indice],
                         *[0 for n in range(indice)])
    
    def __iter__(self):
        return self._Ponteiro(self)
    
    class _Ponteiro:
        def __init__(self, p):
            self.pos = iter(p.coeficientes)
            self.g = p.grau+1
        
        def __next__(self):
            self.g -= 1
            mon = next(self.pos)
            return Polinomio(mon, *[0 for n in range (self.g)],
                             dtype = type(mon))
