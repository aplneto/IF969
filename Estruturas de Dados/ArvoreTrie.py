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
    
    def inserir(self, palavra):
        '''
        Método de inserção das palavras na árvore
        '''
        self.raiz.inserir(palavra)
    
    def inserirtexto(self, texto):
        '''
        Método de de inserção dinâmico de textos palavra a palavra
        '''
        sep = [' ', ',', ';', '.', ':', '!', '?', '\n']  # Lista de separadores
        palavra = ''
        for c in texto:
            if c not in sep:
                palavra += c
            else:
                # O próximo if visa evitar a inserção de strings vazias
                # Isso pode acontecer com o uso de espaços duplos, "...", etc.
                if palavra != '':
                    self.inserir(palavra)
                    palavra = ''
        if palavra != '':
            self.raiz.inserir(palavra)
    
    def pop(self, palavra):
        '''
        Método de remoção de palavra. Remove uma determinada palavra da árvore
        e retorna o valor que o nó guardava antes de ser deletado
        '''
        return self.raiz.remover(palavra)
        
    def __getitem__(self, item):
        '''
        Permite o acesso através de chave, como em dicionário. Por exemplo:
            a = Trie("amor e amar amora")
            a["amor"]
            Out: 1
        '''
        return self.raiz.pesquisar(item)
    
    def __len__(self):
        return len(self.raiz)
    
    def __str__(self):
        return self.raiz.__str__()
    
    def __repr__(self):
        return self.raiz.__repr__()

class _Node():
    '''
    Objeto Nó que armazena os vetores e a contagem
    '''
    def __init__(self):
        self.letras = ndarray(shape = 53, dtype = object)
        self.cont = 0
    
    def folha(self):
        '''
        Método que identifica nós folhas.
        Retorna True caso o nó seja uma folha e False caso não seja.
        '''
        for c in self.letras:
            if c is not None:
                return False
        return True

    def inserir(self, palavra):
        '''
        Método de inserção das palavras na árvore
        '''
        atual = self
        for char in palavra:
            p = atual.__pos(char)
            if atual.letras[p] is None:
                atual.letras[p] = _Node()
            atual = atual.letras[p]
        atual.cont += 1

    def pesquisar(self, palavra):
        '''
        Método de pesquisa das palavras na árvore
        '''
        atual = self
        for char in palavra:
            p = atual.__pos(char)
            if atual.letras[p] is None:
                raise KeyError("Palavra não encontrada")
            atual = atual.letras[p]
        return atual.cont
    
    def remover(self, palavra):
        '''
        Método recursivo de remoção
        '''
        if len(palavra) == 1:
            p = self.__pos(palavra[0])
            nodo = self.letras[p]
            if nodo is None:
                raise KeyError("Palavra não encontrada")
            else:
                num = nodo.cont
                nodo.cont = 0
                if nodo.folha():
                    self.letras[p] = None
                    del nodo
                return num
        else:
            p = self.__pos(palavra[0])
            nodo = self.letras[p]
            if nodo is None:
                raise KeyError("Palavra não encontrada")
            else:
                num = nodo.remover(palavra[1:])
                if nodo.folha() and nodo.cont == 0:
                    self.letras[p] = None
                    del nodo
                return num
        
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
        for c in self.letras:
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
            texto += '"{}"({})'.format(dupla[0], dupla[1])
        return texto
    
    def __repr__(self):
        return "Arvore-Trie([{}])".format(self.__str__())
    
    def __texto(self, atual = "", palavras = []):
        for i in range(52):
            if not self.letras[i] is None:
                if self.letras[i].cont > 0:
                    palavras.append((atual+self.__char(i), self.letras[i].cont))
                self.letras[i].__texto(atual+self.__char(i), palavras)
                