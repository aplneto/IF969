#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sat May 25 20:22:25 2019

Descrição: Código de Classe Auxiliar Plano Cartesiano

Essa classe simula um plano cartesiano e armazena pontos projetados sobre esse
plano.
O objetivo principal dessa classe é facilitar a conversão de pontos num plano
cartesiano para um grafo ponderado não direcionado.

Para melhor aprendizado, use ternos pitagóricos para calcular as distâncias
entre os pontos.

Exemplo: (3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)...
"""

import math
import numpy

class PlanoCartesiano:
    def __init__(self, iteravel = None):
        '''
        Método construtor do Plano Cartesiano
        Apenas para demonstração, a origem do plano será sempre um dos pontos
        
        Args:
            iteravel: (list, tuple, dict, set, generator) objeto iterável
                contendo pares x e y dos pontos 
        '''
        self.__abscissas = [0] #eixo X
        self.__ordenadas = [0] #eixo Y
        self.tam = 0
        if iteravel:
            for x, y in iteravel:
                if x and y:
                    self.adicionar_ponto(x, y)
    
    @property
    def eixo_x(self):
        return self.__abscissas
    
    @property
    def eixo_y(self):
        return self.__ordenadas
        
    def adicionar_ponto(self, x1:int, y1:int):
        '''
        Adiciona um ponto ao plano
        Args:
            x1 (int): coordenada x do ponto
            x2 (int): coordenada y do ponto
        
        Returns:
            int: número correspondente ao ponto
        '''
        self.__abscissas.append(x1)
        self.__ordenadas.append(y1)
        self.tam += 1
        return self.tam
    
    def coordenadas(self, p):
        '''
        Retorna as coordenadas do ponto de índice p.
        
        Warnings:
            O ponto no índice 0 é a origem do plano
        
        Args:
            p (int): índice do ponto p
        
        
        Returns:
            tuple(x, y): onde x e y são as coordenadas do ponto p
        
        Raises:
            IndexError se o ponto p não existir no plano
        '''
        return self.__abscissas[p], self.__ordenadas[p]
    
    def calcular_distancia(self, x1:int, y1:int, x2:int, y2:int):
        '''
        Calcula a distância entre pontos na coordenada x1, y1 e x2, y2
        
        Args:
            x1 (int): coordenada x do primeiro ponto
            y1 (int): coordenada y do primeiro ponto
            x2 (int): coordenada x do segundo ponto
            y2 (int): coordenada y do segundo ponto
        
        Returns:
            float: distância entre as coordenadas
        '''
        return math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    
    def distancia_entre_pontos(self, p1:int, p2:int):
        '''
        Usa o método self.calcular_distancia(x1, y1, x2, y2) para calcular as
        distâncias entre os pontos p1 e p2.
        
        Args:
            p1 (int): índice do primeiro ponto
            p2 (int): índice do segundo ponto
        
        Returns:
            float: distância entre p1 e p2
        
        Raises:
            IndexError se o ponto p1 ou o ponto p2 não estão no plano
        '''
        return self.calcular_distancia(*self.coordenadas(p1),
                                       *self.coordenadas(p2))
    
    def lista_de_adj(self, p):
        '''
        Gera uma lista de adjacências a partir de um ponto do plano.
        
        A lista retornada é composta por tuplas de pares i, d, onde i é
        o índice do ponto vizinho e d é a distância até este ponto, para
        todos os pontos i != p.
        
        Args:
            p (int): índice do ponto
        
        Returns:
            list: lista de pares p, d, sendo p o índice dos demais pontos
                do grafo e d a distância até eles.
        
        Raises:
            IndexError se o ponto não pertencer ao plano
        '''
        return [(i, self.distancia_entre_pontos(p, i)) for i in range(
                1, self.tam+1) if i!=p]
    
    def matriz_de_adj(self):
        '''
        Gera uma matriz de adjacências para todos os pontos no plano.
        
        A matriz retornada tem tamanho nxn, onde n é a quantidade de pontos no
        plano e o valor d na linha i, coluna j, representa a distância entre os
        pontos i e j.
        
        Returns:
            numpy.array: matriz de adjacências shape=(n,n)
        '''
        matriz = numpy.zeros((self.tam+1, self.tam+1))
        for i in range(1, self.tam+1):
            for j in range(1, self.tam+1):
                if i!=j:
                    matriz[i, j] = self.distancia_entre_pontos(i, j)
        return matriz
    
    def index(self, x:int, y:int):
        '''
        Retorna o índice do ponto com as coordenadas x e y.
        Caso o ponto não pertença ao plano, retorna 0.
        
        Args:
            x (int): coordenada x do ponto
            y (int): coordenada y do ponto
        
        Returns:
            int: índice do ponto no plano ou 0, caso o ponto não pertença ao
                plano
        '''
        for p in range(1, self.tam+1):
            if self.__abscissas[p] == x and self.__ordenadas[p] == y:
                return p
        return 0
    
    def __contains__(self, x:int, y:int):
        return bool(self.index(x, y))
        
    def __str__(self):
        return 'x, y: '+', '.join("({0}, {1})".format(self.__abscissas[p],
                                  self.__ordenadas[p]) for p in range (1,
                                                  self.tam+1))
    
    def __repr__(self):
        return self.__class__.__name__+'([{}])'.format(', '.join(
                "({0}, {1})".format(self.__abscissas[p], self.__ordenadas[p])
                for p in range (1, self.tam+1)))

if __name__ == "__main__":
    p = PlanoCartesiano()
    p.adicionar_ponto(1, 1)
    p.adicionar_ponto(4, 5)
    p.adicionar_ponto(7, 9)
    p.adicionar_ponto(6, 13)
    p.adicionar_ponto(10, 13)