#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 04:32:58 2019

@author: aplneto
"""

def busca_em_profundidade(grafo):
    marcados = grafo.tam*[False]
    origens = grafo.tam*[-1]
    for v in range(grafo.tam):
        if not marcados[v]: grafo.__dfs(v, origens, marcados)
    return origens

def __dfs(grafo, v, origens, marcados):
    marcados[v] = True
    for u in grafo.adjacentes(v):
        if not marcados[u]:
            origens[u] = v
            grafo.__dfs(u, origens, marcados)

def busca_em_largura(grafo):
    marcados = grafo.tam*[False]
    origens = grafo.tam*[-1]
    vertices = []
    for i in range(grafo.tam):
        if not marcados[i]:
            vertices.append(i)
            marcados[i] = True
            while len(vertices) > 0:
                v = vertices.pop(0)
                for u in grafo.__adj(v):
                    if not marcados[u]:
                        marcados[u] = True
                        origens[u] = v
                        vertices.append(u)
                        return origens