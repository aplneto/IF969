#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br
                    Created on Thu Jun 20 22:03:45 2019
Descrição: Implementação do Algoritmo de Dijkstra para solução do problema de
menor caminho em grafos direcionados.

                        Licenca: The MIT License (MIT)
                    Copyright(c) 2019 Antônio Paulino de Lima Neto
"""
import numpy

def dijkstra(grafo, inicial = 0):
    pesos = numpy.full((grafo.tam), numpy.inf)
    pesos[0] = 0
    origens = numpy.full((grafo.tam), -1)
    vertices = list(range(grafo.tam))
    
    def relaxar(origem, aresta):
        nonlocal pesos, origens
        destino, peso_aresta = aresta
        if destino in vertices:
            if pesos[origem] + peso_aresta < pesos[destino]:
                pesos[destino] = pesos[origem] + peso_aresta
                origens[destino] = origem
    
    while vertices:
        vertice = vertices.pop(0)
        for aresta in grafo.adjacentes(vertice):
            relaxar(vertice, aresta)
        heapify_vertices(vertices, pesos)
            
    return list(zip(list(range(grafo.tam)), pesos))

# Funções Auxiliares

pai = lambda i: (i-1)//2
esquerda = lambda i: (i*2)+1
direita = lambda i: (i*2)+2

def heapify_vertices(vertices, pesos):
    '''Constrói um heap a partir de um dado vetor
    '''
    tam = len(vertices)
    i = pai(tam)
    while i >= 0:
        heapify_vertice_down(i, vertices, pesos)
        i -= 1

def heap_pop_vertice(vertices, pesos):
    vertices[0], vertices[-1] = vertices[-1], vertices[0]
    v = vertices.pop(0)
    heapify_vertice_down(0, vertices, pesos)
    return v

def heapify_vertice_down(v, vertices, pesos):
    
    peso = lambda i: pesos[i]
    tam = len(vertices)
    
    filho = esquerda(v)
    while filho < tam:
        d = direita(v)
        if filho < (tam-1) and peso(vertices[filho]) > peso(vertices[d]): filho = d
        if peso(vertices[filho]) > peso(vertices[v]): break
        vertices[filho], vertices[v] = vertices[v], vertices[filho]
        v = filho
        filho = esquerda(v)
        

def heapify_vertice_up(v, vertices, pesos):
    peso = lambda i: pesos[i]
    while v > 0 and peso(vertices[v]) < peso(vertices[pai(v)]):
        vertices[v], vertices[pai(v)] = vertices[pai(v)], vertices[v]
        v = pai(v)

def are_vertices_heapified(vertices, pesos):
    peso = lambda i: pesos[i]
    tam = len(vertices)
    v = tam//2
    while v < tam:
        if peso(vertices[v]) < peso(vertices[pai(v)]):
            return False
        v += 1
    return True