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
        '''
        Método construtor do grafo
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
        '''
        Retorna True se o grafo for ponderado
        '''
        return self.__ponderado
    
    @property
    def direcionado(self):
        '''
        Retorna True se o grafo for direcionado
        '''
        return self.__direcionado
    
    def inserir_vertice(self):
        '''
        Insere um vértice na lista de adjcências
        '''
        self.__lista_adj.append([])
        self.tam += 1
        return self.tam-1
    
    def inserir_aresta(self, i, j, p = 1):
        '''
        Insere uma aresta se o grafo não for direcionado
        '''
        if i >= self.tam or self.__lista_adj[i] == None: raise IndexError
        if j >= self.tam or self.__lista_adj[i] == None: raise IndexError
        self.__lista_adj[i].append((j,p))
        if not self.__direcionado:
            self.__lista_adj[j].append((i,p))
    
    def remover_aresta(self, i, j):
        '''
        
        '''
        if i >= self.tam or self.__lista_adj[i] == None: raise IndexError
        if j >= self.tam or self.__lista_adj[i] == None: raise IndexError
        for aresta in self.__lista_adj[i]:
            if aresta[0] == j:
                self.__lista_adj[i].remove(aresta)
                break
        if not self.direcionado:
            for aresta in self.__lista_adj[j]:
                if aresta[0] == i:
                    self.__lista_adj[j].remove(aresta)
                    break
    
    def adjacentes(self, i):
        '''
        Retorna a lista de vértices adjacentes
        '''
        if i >= self.tam: raise ArithmeticError
        if self.__ponderado:
            return self.__lista_adj[i]
        else:
            l = [x[0] for x in self.__lista_adj[i]]
            return l
    
    def __adj(self, i):
        if i >= self.tam: raise ArithmeticError
        l = [x[0] for x in self.__lista_adj[i]]
        return l        
    
    def menor_aresta(self):
        '''Verifica a aresta de menor peso
        '''
        menor_aresta = (-1, -1, float('inf'))
        for v in range(self.tam):
            for i in range(self.tam):
                if self.__lista_adj[v][i][1] < menor_aresta[1]:
                    menor_aresta = (v, i, self.__lista_adj[v][i][1])
        if menor_aresta == (-1, -1, float('inf')): raise ArithmeticError
        return menor_aresta and not self.__ponderado or menor_aresta[:-1]

    def maior_aresta(self):
        '''Verifica a aresta de maior peso
        '''
        maior_aresta = (-1, -1, -float('inf'))
        for v in range(self.tam):
            for i in range(self.tam):
                if self.__lista_adj[v][i][1] > maior_aresta[1]:
                    maior_aresta = (v, i, self.__lista_adj[v][i][1])
        if maior_aresta == (-1, -1, -float('inf')): raise ArithmeticError
        return maior_aresta and not self.__ponderado or maior_aresta[:-1]
    
    def grau_de_saida(self, i):
        '''Retorna a quantidade de vértices adjacentes
        '''
        return len(self.__lista_adj[i])
    
    def grau_de_entrada(self, i):
        entrada = 0
        for v in self.__lista_adj:
            for a in v:
                if a[0] == i: entrada+=1
        return entrada
    
    def aresta(self, i, j):
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