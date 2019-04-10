# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:00:08 2019

@author: apln2
"""

class Node:
    def __init__(self, valor, ant = None, suc = None):
        self.valor = valor
        self.ant = ant
        self.suc = suc
    
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.valor)

class Fila:
    def __init__(self):
        self.primeiro = self.ultimo = Node(None)
    
    def inserir(self, valor):
        self.ultimo.suc = Node(valor, ant = self.ultimo, suc = None)
        self.ultimo = self.ultimo.suc
    
    def remover(self):
        '''
        filas removem elementos apenas no início
        '''
        if self.primeiro == self.ultimo:
            raise IndexError ("Impossível remover itens de uma fila vazia")
        aux = self.primeiro.suc
        valor = aux.valor
        self.primeiro.suc = aux.suc
        if aux.suc is not None:
            aux.suc.ant = self.primeiro
        else:
            self.ultimo = self.primeiro
        aux.suc = aux.ant = None
        del aux
        return valor
    
    def vazia(self):
        return self.primeiro == self.ultimo
        
    def __repr__(self):
        '''
        digite o nome do objeto para observar o que acontece
        '''
        pos = self.primeiro.suc
        _str = ''
        while pos is not None:
            if _str: _str += ', '
            _str += str(pos.valor)
            pos = pos.suc
        return '['+_str+']'
    
    def __str__(self):
        if self.primeiro == self.ultimo:
            return '0'
        else:
            return str(self.primeiro.suc.valor)

if __name__ == "__main__":
    T = int(input())
    for c in range (T):
        print("Caso {}:".format(c+1))
        f = Fila()
        p = Fila()
        num_comandos = int(input())
        for i in range (num_comandos):
            comando = input()
            if comando[0] == 'f':
                f.inserir(int(comando[2:]))
            elif comando[0] == 'p':
                p.inserir(int(comando[2:]))
            elif comando[0] == 'A':
                if f.vazia():
                    p.remover()
                else:
                    f.remover()
            elif comando[0] == 'B':
                if p.vazia():
                    f.remover()
                else:
                    p.remover()
            else:
                print("{} {}".format(f, p))