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

from numpy import ndarray

class Trie():
    '''
    Objeto árvore Trie básica usada para contagem de palavras.
    Modelo utilizado para contagem de palavras apenas contendo letras
    maiúsculas e minúsculas.
    '''
    def __init__(self, texto = ''):
        self.raiz = _Node()
        self.inserirtexto(texto)
    
    def inserirpalavra(self, palavra):
        '''
        Método de inserção das palavras na árvore
        '''
        atual = self.raiz
        for char in palavra:
            p = self.__pos(char)
            if atual.pos[p] is None:
                atual.pos[p] = _Node()
            atual = atual.pos[p]
        atual.cont += 1
    
    def inserirtexto(self, texto):
        '''
        Método de de inserção dinâmico de textos palavra a palavra
        '''
        sep = [' ', ',', ';', '.', ':', '!', '?']  # Lista de separadores
        palavra = ''
        for c in texto:
            if c not in sep:
                palavra += c
            else:
                # O próximo if visa evitar a inserção de strings vazias
                # Isso pode acontecer com o uso de espaços duplos, "...", etc.
                if palavra != '':
                    self.inserirpalavra(palavra)
                    palavra = ''
        if palavra != '':
            self.inserirpalavra(palavra)
            
    def pesquisarpalavra(self, palavra):
        '''
        Método de pesquisa das palavras na árvore
        '''
        atual = self.raiz
        for char in palavra:
            p = self.__pos(char)
            if atual.pos[p] is None:
                return 0
            atual = atual.pos[p]
        return atual.cont
    
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
        
    def __getitem__(self, item):
        '''
        Permite o acesso através de chave, como em dicionário. Por exemplo:
            a = Trie("amor e amar amora")
            a["amor"]
            Out: 1
        '''
        return self.pesquisarpalavra(item)
    
    def __len__(self):
        return len(self.raiz)
    
    def __str__(self):
        return self.raiz.__str__()
    
    def __repr__(self):
        return self.raiz.__repr__()

class _Node():
    '''
    Objeto Nó que armazena as letras e informações de da árvore.
    '''
    def __init__(self):
        self.pos = ndarray(shape = 52, dtype = object)
        self.cont = 0
    
    def __char(self, num):
        '''
        Função inversa a de localização da posição. Retorna o caractere
        correspondente baseado no índice de sua posição.
        '''
        if num >= 0 and num <= 25:
            return chr(num + ord('a'))
        elif num >= 26 and num <= 51:
            return chr(num+ord('A')-26)
        else:
            return '?'
    
    def __len__(self):
        valor = 0
        for c in self.pos:
            if not c is None:
                valor += c.__len__()
                valor += c.cont
        return valor
    
    def __str__(self):
        info = []
        self.__texto(palavras = info)
        texto = ""
        for dupla in info:
            if texto:
                texto += ", "
            texto += "{}({})".format(dupla[0], dupla[1])
        return texto
    
    def __repr__(self):
        return "Arvore-Trie[{}]".format(self.__str__())
    
    def __texto(self, atual = "", palavras = []):
        for i in range(52):
            if not self.pos[i] is None:
                if self.pos[i].cont > 0:
                    palavras.append((atual+self.__char(i), self.pos[i].cont))
                self.pos[i].__texto(atual+self.__char(i), palavras)
                