# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Tue Jul 10 02:48:00 2018
                            
Descricao: ...

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

from numpy import ndarray

class _Node():
    '''
    Classe auxiliar para nós da árvore de prefixos
    '''
    def __init__(self):
        self.__pos = ndarray(shape = 53, dtype = object)
        self.folha = False

    def __pos(self, char):
        '''
        Função auxiliar que retorna a posição de um determinado caractere no
        vetor de caracteres de cada nó.
        '''
        if char >= 'a' and char <= 'z':
            return ord(char)-ord('a')
        elif char >= 'A' and char <= 'Z':
            return ord(char)-ord('A')+26
        else:
            return 52

class RadixTree():
    '''
    Classe da árvore Patrícia
    '''
    def __init__(self, texto = ""):
        self.raiz = _Node()
        self.inserirtexto(texto)
    
    def inserirpalavra(self, palavra):
        pass
    
    def inserirtexto(self, texto):
        pass