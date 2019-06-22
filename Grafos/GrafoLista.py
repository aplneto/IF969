#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                        Created on Fri Jun 26 04:31:08 2019

Descrição: Script contento a classe Grafo, representada através de Lista de
    Adjacências.

Licenca: The MIT License (MIT)

                       Copyright(c) 2019 Antônio Paulino de Lima Neto

"""


class TADGrafoLista:
    '''
    TAD Grafo representado através de Lista de Adjacências
    '''
    def __init__(self, v = 0, **kwargs):
        '''Método construtor do grafo
        
        Args:
            v (int): número de vértices
        kwargs:
            direcionado (bool): representa a existência de direção nas aretas
                do grafo
            ponderado (bool): representa a existência de pesos nas arestas do
                grafo
            iteravel (iteravel): objeto iteravel a partir do qual o grafo pode
                ser construido. Deve conter tuplas de dois ou três elementos,
                representando suas arestas.
        '''
        self.__lista_adj = [[] for x in range(v)]
        self.tam = v
        self.__direcionado = kwargs.get('direcionado', False)
        self.__ponderado = kwargs.get('ponderado', False)
        iteravel = kwargs.get('iteravel', None)
        if iteravel is not None:
            self.__construir_grafo(iteravel)
    
    @property
    def ponderado(self):
        return self.__ponderado
    
    @property
    def direcionado(self):
        return self.__direcionado
    
    def inserir_vertice(self):
        '''Método de criação de vértices
        
        Criar uma nova lista de adjacências vazia e retorna o índice do vértice
        criado.
        
        Returns:
            (int): índice do novo vértice
        '''
        self.__lista_adj.append([])
        self.tam += 1
        return self.tam-1
    
    def inserir_aresta(self, i, j, p = 1):
        '''Método de criação de Arestas
        
        Insere uma aresta na lista de adjacências de i contendo o valor de j e
        o peso da aresta.
        Se o grafo não for direcionado, a tupla contendo i e p é também
        adicionada a lista de adjacências de j.
        Args:
            i (int): índice do vértice de origem
            j (int): índice do vértice de destino
            p (float): peso da aresta
        '''
        if i >= self.tam: raise IndexError(f"#{i} não pertence ao vértice")
        if j >= self.tam: raise IndexError(f"#{j} não pertence ao vértice")
        self.__lista_adj[i].append((j,p))
        if not self.__direcionado: self.__lista_adj[j].append((i,p))
    
    def remover_aresta(self, i, j, p):
        '''Método de remoção de arestas
        
        Remove da lista de adjacências de i e retorna a primeira aresta
        direcionada a j com peso p.
        Caso o grafo não seja direcionado, remove também a aresta da lista de
        adjacências de j.
        Args:
            i (int): índice do vértice de origem
            j (int): índice do vértice de destino
            p (int): peso da aresta
        Returns:
            (tuple): tupla contendo i, j e p, caso a aresta tenha sido removida
            None: caso a aresta não exista
        '''
        if i >= self.tam: raise IndexError(f"#{i} não pertence ao vértice")
        if j >= self.tam: raise IndexError(f"#{j} não pertence ao vértice")
        for aresta in self.__lista_adj[i]:
            if aresta == (j, p):
                self.__lista_adj[i].remove(aresta)
                if not self.direcionado: self.__lista_adj[j].remove((i, p))
                return (i, j, p)
        return None
    
    def arestas_adjacentes(self, i):
        '''
        Retorna a lista de arestas adjacentes ao vértice i
        
        Args:
            i (int): índice do vértice i
        Returns:
            (list): contendo os tuplas com os vértices de destino pesos das
                arestas se o grafo for ponderado. Caso não, retorna uma lista
                com os índices dos vértices de destino.
        '''
        if i >= self.tam: raise IndexError(f"#{i} não percence ao vértice")
        return self.__lista_adj[i]
    
    def vertices_adjacentes(self, i):
        '''
        Retorna a lista de vértices adjacentes ao vértice
        Args:
            i (int): índice do vértice i
        Returns:
            (list): contendo os índices dos vértices adjacentes ao vértice i
        '''
        if i >= self.tam: raise IndexError(f"#{i} não percence ao vértice")
        return [x[0] for x in self.__lista_adj[i]]
    
    def grau_de_saida(self, i):
        '''Retorna a quantidade de vértices adjacentes ao vértice i
        
        Args:
            i (int): índice do vértice
        Returns:
            (int): gráu de saída do vértice i
        '''
        return len(self.__lista_adj[i])
    
    def grau_de_entrada(self, i):
        entrada = 0
        for v in self.__lista_adj:
            for a in v:
                if a[0] == i: entrada+=1
        return entrada
    
    def aresta(self, i, j):
        '''Método de verificação de existência de aresta
        
        Procura por uma aresta direcionada a j na lista de adjacências de i.
        
        Args:
            i (int): índice do vértice de origem
            j (int): índice do vértice de saída
        Returns:
            (bool): existência de aresta de i para j
        '''
        for t in self.__lista_adj[i]:
            if t[0] == j: return True
        return False
    
    def __contains__(self, i):
        if i < self.tam:
            return self.__lista_adj[i] != -1
        else:
            return False
    
    def __construir_grafo(self, iteravel):
        '''
        Método que constróio o grafo a partir de um iterável contendo as
        arestas
        Args:
            iteravel: objeto iteravel contendo tuplas de 2 ou 3 elementos,
                cujos elementos sejam valores inteiros.
        '''
        for tupla in iteravel:
            while not (tupla[0] in self or tupla[1] in self):
                self.inserir_vertice()
            self.inserir_aresta(*tupla)
    
    def __getitem__(self, i):
        return tuple(self.__lista_adj[i])
    
    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__,
                self.__lista_adj.__repr__())
    
    def __str__(self):
        l = []
        for v in range(self.tam):
            if v != -1:
                l.append("{0}: {1}".format(v, ', '.join(str(x)\
                         for x in self.adjacentes(v))))
        return "\n".join(l)