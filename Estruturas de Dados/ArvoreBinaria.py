# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Fri Jul 13 14:02:20 2018
                            
Descricao: Árvore Binária

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

#==============================================================================
#
#   Representação gráfica simples de uma árvore binária, onde as chaves são
# números inteiros e os valores são as strings contendo os números ecritos por
#                                     extenso
#
#
#                                   (5, "cinco")
#                                    /        \
#                         (4, "quatro")      (10, "dez")
#                          /      \            /      \
#                  (2, "dois")   None    (6, "seis") None
#                    /     \              /       \
#              (1, "um") (3, "três")  None (7, "oito")
#                /   \     /     \           /      \
#             None  None None  None        None   (9, "nove")
#                                                   /      \
#                                             (8, "oito)   None
#                                               /    \
#                                             None  None
#
#==============================================================================

class _No:
    '''
    Classe auxiliar nó.
    Guarda a chave, o valor e dois filhos (menores a esquerda e maiores a
    direita).
    '''
    def __init__(self, chave, valor, esquerda = None, direita = None):
        self.valor = valor
        self.chave = chave
        self.e = esquerda
        self.d = direita
    
    def __str__(self):
        return "{}:{}".format(self.chave.__repr__(), self.valor.__repr__())
    
    def __repr__(self):
        return self.__str__()

class Arvore:
    '''
    Classe principal de árvore Binária.
    Essa classe se comporta como um dicionário de Python, desde que os valores
    fornecidos como chave possam ser comparados entre si.
    A árvore pode ser construída vazia ou através de um iterável contendo
    pares, como por exemplo uma lista de tuplas onde cada tupla é composta por
    chave como elemento 0 e valor como elemento 1.
    '''
    def __init__(self, iteravel = None):
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
    
    def inserir(self, chave, valor):
        '''
        O método de inserção precisa ser recursivo, logo, precisa receber
        também qual o primeiro nóe em que o valor será inserido. Por isso, para
        facilitar o trabalho do usuário, criamos um método para chamar o
        verdadeiro método de inserção, que é uma função privada.
        '''
        self.raiz = self.__inserir(self.raiz, chave, valor)
    
    def __inserir(self, no, chave, valor):
        '''
        Note que essa função só instancia um novo nó quando encontra um nó que
        não tenha valor (no == None). Até lá, depois da chamada de recursão, a
        função sempre retorna o nó atual.
        '''
        if no is None:
            return _No(chave, valor)
        elif chave > no.chave:
            no.d = self.__inserir(no.d, chave, valor)
        elif chave < no.chave:
            no.e = self.__inserir(no.e, chave, valor)
        else:
            no.valor = valor
        return no