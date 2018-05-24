# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                        Created on Thu May 24 01:28:08 2018

Descricao: Códigos das classes de dado abstratas grafos com as suas funções
básicas implementadas

Licenca: The MIT License (MIT)

                       Copyright(c) 2018 Antônio Paulino de Lima Neto

"""

class GrafoMatriz(object):
    '''
    TAD Grafo representado através de Matriz de Adjacências.
    '''
    def __init__(self, v = 0, direcionado = False):
        self.vertices = v
        self.adj = [[0]*v for x in range (v)]
        self.__dir = direcionado
    
    def inserir_aresta(self, u, v):
        '''
        Função de inserção de aresta. Quando o grafo não é direcionado, a
        inserção acontece nos valores uxv e vxu da matriz para cada aresta.
        '''
        try:
            self.adj[u][v] = 1
            if not self.__dir:
                self.adj[v][u] = 1
        except IndexError:
            raise IndexError ("Um ou mais vértices não pertencem ao grafo")
    
    def verificar_aresta(self, u, v):
        try:
            return bool(self.ad[u][v])
        except IndexError:
            raise IndexError ("Um ou mais vértices não pertencem ao grafo")
    
    def adjacentes(self, v):
        '''
        Função retorna uma lista de vértices adjacentes ao vertice parâmetro.
        '''
        try:
            adj = []
            for u, a in enumerate(self.adj[v]):
                if a: adj.append(u)
            return adj
        except:
            IndexError ("Vértice não pertence ao grafo")
    
    def remover_aresta(self, u, v):
        try:
            if self.adj[u][v]:
                self.adj[u][v] = 0
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
        for u in range (self.vertices):
            for v in range(self.vertices):
                if self.__dir:
                    arestas += self.adj[u][v]
                else:
                    if u <= v:
                        arestas += self.adj[u][v]
        return arestas
    
    def direcionado(self):
        '''
        Retorna True se o gráfico for direcionado, False se não.
        '''
        return self.__dir
    
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