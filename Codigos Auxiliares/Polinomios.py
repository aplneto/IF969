# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sat Jun  2 11:38:19 2018

Descrição: Código de Classe Auxiliar Polinômios
"""

class Polinomio():
    '''
    Classe auxiliar Polinomio
    '''
    def __init__(self, grau, *coeficientes):
        '''
        Classe polinomio recebe como parâmetros o grau do monomio de maior grau
        e os coeficientes de todos os monomios.
        A exemplo, o polinômio 2x²+3x-1 seria instânciado da seguinte forma:
            Polinomio = (2, 2, 3, -1) ou ainda Polinomio = (2, [2, 3, -1])
        '''
        self.grau = grau
        self.coeficientes = list()
        aux = 0
        if len(coeficientes) == 1 and type(coeficientes[0]) == list:
            self.coeficientes = coeficientes[0]
        else:
            for coeficiente in coeficientes:
                self.coeficientes.append(coeficiente)
                aux += 1
                if aux >= (self.grau+1):
                    break
        while len(self.coeficientes) > 0 and self.coeficientes[0] == 0:
            aux = self.coeficientes.pop(0)
            self.grau -= 1
            del aux
            
    def __derivada(self):
        '''
        Retorna o polinomio correspondente a própria derivada
        '''
        aux = 0
        coeficientes = list()
        for coeficiente in self.coeficientes:
            coeficientes.append(coeficiente*(self.grau - aux))
            aux +=1
        return Polinomio(self.grau-1, *coeficientes)
    
    def __call__(self, x):
        '''
        Retorna o valor de F para o parametro x
        '''
        resultado = 0.0
        aux = 0
        for coeficiente in self.coeficientes:
            resultado += coeficiente*(x**(self.grau-aux))
            aux += 1
        return resultado
            
    def __repr__(self):
        func = ''
        aux = 0
        for c in self.coeficientes:
            if func and c>0:
                func += '+'
            if c and aux < self.grau-1:
                func += '{0}x^{1}'.format(c if c!=1 else '', self.grau-aux)
            elif c and aux == self.grau-1:
                func += '{0}x'.format(c if c!=1 else '')
            elif c:
                func+= '{}'.format(c)
            aux += 1
        return func and func or '0'
    
    def __str__(self):
        return "F(x) = {}".format(self.__repr__())
    
    def __getattr__(self, key):
        if key == 'derivada':
            return self.__derivada()

    def raiz(self, x0, tol):
        '''
        Encontra uma aproximação para a raiz do polinômio a partir do método de
        Newton-Raphson
        x0: valor inicial positivo aproximado da raiz
        tol: tolerância, valor máximo para x0
        '''
        while abs(self(x0)) > tol:
            x0 -= self(x0)/self.derivada(x0)
        return x0

def newton_raphson(lista_coef, tol, x0):
    '''
    Método de Newton-Raphson que conta as iterações
    lista_coef: lista dos coeficientes do maior grau ao menor
    tol: valor minimo aceitável de f(x) (tol >0)
    x0: valor inicial aproximado da raiz
    '''
    f = Polinomio(len(lista_coef)-1, *lista_coef)
    itr = 0
    x = x0
    while abs(f(x)) > tol:
        x -= f(x)/f.derivada(x)
        itr += 1
    print("x = {0}\nEm {1} iterações.".format(x, itr))