# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Thu Jul 19 10:32:14 2018
                            
Descrição: Fila de Prioridades são estruturas de dados lineares do tipo FIFO 
(First-In First-Out ou primeiro a entrar, primeiro a sair). Nessas estruturas a
inserção ocorre sempre em um extremo e a remoção em outro, obedecendo assim a
ordem dechegada. Nesse tipo de Estrutura, as operação tem nomes diferentes, o
"append" passa a ser chamado de enqueue (enfileirar) e o pop de dequeue
(desenfileirar) também passando a acontecer sempre na primeira posição.

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

class _No:
    '''
    Classe auxiliar nó usada para guardar os elementos e compor a estrutura
    linear.
    '''
    def __init__(self, valor, proximo = None):
        self.valor = valor
        self.proximo = proximo
    
    def __str__(self):
        return self.valor.__str__()
    
    def __repr__(self):
        return "_No({})".format(self.valor.__repr__())

class Fila:
    '''
    Classe principal fila.
    Funciona de maneira similar a uma lista de encadeamento simples.
    '''
    def __init__(self, iteravel = None, **kwargs):
        self.primeiro = self.ultimo = _No(None)
        self.lim = kwargs.get("lim", float('inf'))
        self.__tam = 0
    
    def enqueue(self, valor):
        '''
        Enfileira funciona exatamente como a operação de anexar (append) das
        listas encadeadas, adicionando um novo nó ao fim da lista.
        '''
        if self.__tam < self.lim:
            self.ultimo.proximo = _No(valor)
            self.ultimo = self.ultimo.proximo
            self.__tam += 1
        else:
            raise ValueError ("capacidade máxima da fila alcançada")
    
    def dequeue(self, valor):
        '''
        O processo de desenfileirar acontece sempre no ínicio da lista,
        respeitando a ordem de entrada dos valores.
        '''
        if self.primeiro == self.ultimo:
            raise IndexError("fila vazia")
        else:
            aux = self.primeiro.proximo
            self.primeiro.proximo = aux.proximo
            aux.proximo = None
            valor = aux.valor
            del aux
            self.__tam -= 1
            return valor
    
    # Métodos Especiais
    
    def __repr__(self):
        no = self.primeiro.proximo
        msg = ''
        while no is not None:
            if msg: msg += ', '
            msg += no.__repr__()
            no = no.proximo
        return '[{}]'.format(msg)
    
    def __str__(self):
        return self.__repr__()
    
    def __getitem__(self, i):
        cont = -1
        no = self.primeiro
        while cont < i:
            if no.proximo is None:
                raise IndexError ("índice fora de alcance")
            else:
                no = no.proximo
        return no.valor
    
    def __len__(self):
        return self.__tam
    
    def __contains__(self, item):
        no = self.primeiro.proximo
        while not no is None:
            if no.valor == item:
                return True
            no = no.proximo
        return False