# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Tue May 15 16:09:17 2018
                            
Descricao: ...

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto

"""

class Trie():
    '''
    Objeto árvore Trie básica usada para contagem de palavras.
    Obs.: Modelo com leitura apenas de letras minúsculas e sem acento.
    '''
    def __init__(self, num = 0, fim = False, **kwargs):
        self.raiz = True
        self.letra = [None]*26
        self.num = num
        self.fim = fim
    
    def inserir (self, palavra):
        pos = lambda c: ord(c)-ord('a')
        atual = self
        for char in palavra:
            if atual.letra[pos(char)] is None:
                atual.letra[pos(char)] = Trie()
                atual.letra[pos(char)].raiz = False
            atual = atual.letra[pos(char)]
        atual.num += 1
        atual.fim = True
    
    def pesquisar (self, palavra):
        pos = lambda c: ord(c) - ord('a')
        atual = self
        for char in palavra:
            if atual.letra[pos(char)] is None:
                raise KeyError
            atual = atual.letra[pos(char)]
        if not atual.fim:
            raise KeyError
        return atual.num