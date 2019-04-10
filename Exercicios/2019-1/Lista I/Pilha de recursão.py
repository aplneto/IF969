# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:30:42 2019

@author: apln2
"""

class Node:
    def __init__(self, valor, ant = None, suc = None):
        self.valor = valor
        self.ant = ant
        self.suc = suc
    
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.valor)

class Pilha:
    def __init__(self):
        self.primeiro = self.ultimo = Node(None)
    
    def inserir(self, valor):
        '''
        As inserções e remoções da classe pilha são sempre no fim da estrutura
        '''
        self.ultimo.suc = Node(valor, ant = self.ultimo, suc = None)
        self.ultimo = self.ultimo.suc
    
    def remover(self):
        if self.primeiro == self.ultimo:
            raise IndexError('Impossível remover de uma pilha vazia')
        aux = self.ultimo
        valor = aux.valor
        self.ultimo = aux.ant
        self.ultimo.suc = aux.suc
        aux.ant = None
        del aux
        return valor
        
    
    def __str__(self):
        _str = ''
        pos = self.primeiro.suc
        while pos is not None:
            if _str: _str += ', '
            _str += pos.valor.__str__()
            pos = pos.suc
        return '[{}]'.format(_str)
    
    def vazia(self):
        return self.primeiro == self.ultimo

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print("Conjunto #{}".format(t+1))
        entrada = input()
        pilha = Pilha()
        comandos = [x for x in entrada.split(' ') if x != '']
        while True:
            for c in comandos:
                if c == 'return':
                    print(pilha.remover())
                else:
                    pilha.inserir(c)
            if not pilha.vazia():
                entrada = input()
                comandos = [x for x in entrada.split(' ') if x != '']
            else:
                break