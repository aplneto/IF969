#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                        Created on Fri Jun 21 04:32:58 2019

Descrição: Busca em largura e profundidade são algoritmos de busca em grafos.

Licenca: The MIT License (MIT)

                       Copyright(c) 2019 Antônio Paulino de Lima Neto

"""

def busca_em_profundidade(grafo):
    '''Função de busca em profunidade
    
    Intuitivamente, na busca em profunidade, a busca começa a partir da raiz do
    grafo ou de um nó inicial arbitrário (neste caso, o nó 0), explorando seus
    ramos o tanto quanto possível antes de retroceder.
    
    Args:
        grafo (object): objeto do tipo grafo no qual a busca será realizada.
    Returns:
        (list): lista contendo o vetor de origens na busca em profunidade.
    '''
    
    def __dfs(grafo, v, origens, marcados):
        '''Função de busca auxiliar
        
        Realiza a busca de forma recursiva, marcando o vetor de origens e o
        vetor auxiliar de marcação.

        Args:
            grafo (object): objeto do tipo grafo no qual a busca será
                realizada;
            v (int): índice do vértice cinza atual;
            origens (list): vetor de origens;
            marcados (list): vetor auxiliar de marcação de vértices brancos
                (False) e vértices pretos (True).
        Returns:
            origens (list): retorna o vetor de origens com as respectivas
                origens de cada um dos vértices.
        '''
        marcados[v] = True
        for u in grafo.vertices_adjacentes(v):
            if not marcados[u]:
                origens[u] = v
                __dfs(grafo, u, origens, marcados)
            
    marcados = grafo.tam*[False]
    origens = grafo.tam*[-1]
    for v in range(grafo.tam):
        if not marcados[v]: __dfs(grafo, v, origens, marcados)
    return origens

def busca_em_largura(grafo):
    '''Função de busca em largura
    
    Intuitivamente a busca em largura começa a partir da raiz de um grafo-
    árvore ou a partir de uma raiz abstrada. A busca é feita em toda a
    vizinhança de vértices adjacentes a esta raiz antes de seguir para o
    próximo vértice.
    
    Args:
        grafo (objetc): objeto do tipo grafo no qual a busca será realizada.
    Returns:
        origens (list): vetor de origens de cada um dos vértices.
    '''
    marcados = grafo.tam*[False]
    origens = grafo.tam*[-1]
    vertices = []
    for i in range(grafo.tam):
        if not marcados[i]:
            vertices.append(i)
            marcados[i] = True
            while len(vertices) > 0:
                v = vertices.pop(0)
                for u in grafo.vertices_adjacentes(v):
                    if not marcados[u]:
                        marcados[u] = True
                        origens[u] = v
                        vertices.append(u)
    return origens