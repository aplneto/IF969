# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                        Created on Thu May 24 01:28:08 2018

Descrição: Script contento a classe Grafo, representada através de Matriz de
    Adjacências.

Licenca: The MIT License (MIT)

                       Copyright(c) 2018 Antônio Paulino de Lima Neto

"""

import numpy

class TADGrafoMatriz:
    '''
    TAD Grafo representado através de Matriz de Adjacências.
    '''
    def __init__(self, v = 0, **kwargs):
        ''' Método Construtor do Grafo por Matriz
        
        Args:
            v (int): número de vértices
        Kwargs:
            direcionado (bool): define se o grafo é direcionado ou não
            ponderado (bool): define se o grafo é ponderado ou não
        '''
        self.__v = v
        self.__matriz_adj = numpy.zeros((v, v))
        self.__dir = kwargs.get('direcionado', False)
        self.__pond = kwargs.get('ponderado', False)
    
    def inserir_aresta(self, i, j, p = 1):
        '''
        Função de inserção de aresta. Quando o grafo não é direcionado, a
        inserção acontece nos valores uxv e vxu da matriz para cada aresta.
        Args:
            i (int): vértice de origem
            j (int): vértice de destino
            p (int): peso
        '''
        try:
            self.__matriz_adj[i][j] = p
            if not self.__dir:
                self.__matriz_adj[j][i] = p
        except IndexError:
            raise IndexError ("Um ou mais vértices não pertencem ao grafo")
    
    def aresta(self, i, j):
        '''
        Verifica se existe uma aresta entre dois vértices
        Args:
            i (int): vértice de origem
            j (int): vértice de destino
        '''
        try:
            return bool(self.__matriz_adj[i][j])
        except IndexError:
            raise IndexError ("Um ou mais vértices não pertencem ao grafo")
    
    def adjacentes(self, i):
        '''
        Retorna uma lista de vértices adjacentes ao vertice parâmetro.
        Args:
            i (int): índice do vértice
        '''
        try:
            adj = list(self.__matriz_adj[i])
            if self.ponderado:
                return list((i, v) for i, v in enumerate(adj) if v)
            else:
                return list(i for i, v in enumerate(adj) if v)
        except:
            IndexError ("Vértice não pertence ao grafo")
    
    def remover_aresta(self, i, j):
        try:
            a = self.__matriz_adj[i][j]
            if a:
                self.__matriz_adj[i][j] = 0
                if not self.direcionado:
                    self.__matriz_adj[j][i] = 0
                return a
            else:
                raise KeyError ("Aresta não pertence ao grafo")
        except IndexError:
            raise IndexError ("Um ou mais vértices não pertencem ao grafo")
    
    def contar_arestas(self):
        '''
        Função que retorna o número de arestas do grafo.
        Quando o grafo não é direcionado, a função contabilza apenas o
        triângulo superior, uma vez que a matriz é espelhada.
        '''
        arestas = 0
        for i in range (self.__v):
            for j in range(self.__v):
                if not(self.ponderado and i+j == self.__v):
                    arestas += bool(self.__matriz_adj[i][j])
        return arestas
    
    @property
    def direcionado(self):
        return self.__dir
    
    @property
    def ponderado(self):
        return self.__pond
    
    @property
    def matriz_de_adjacencias(self):
        return self.__matriz_adj
    
    def __len__(self):
        return self.vertices
    
    def __str__(self):
        string = '   '
        for n in range (self.vertices):
            string += str(n)
            if n < self.vertices-1:
                string += ' '
            else:
                string += '\n'
        for i, u in enumerate(self.adj):
            string += '{}: '.format(i)
            for cont, v in enumerate(u):
                string += str(v)
                if cont < self.vertices-1:
                    string+=' '
                elif i < self.vertices-1:
                    string+='\n'
        return string
    
    def __repr__(self):
        return str(self)