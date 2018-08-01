# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Inform�tica (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Ant�nio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Fri Jul 13 14:02:20 2018
                            
Descricao: arvore Binaria Balanceada (arvore 2-3)

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antonio Paulino de Lima Neto
"""
class _2No:
    '''
    Classe auxiliar de N� simples (2-Node)
    Guarda um valor e uma chave, al�m de refer�ncias para as sub�rvores a
    esquerda e direita, como na �rvore bin�ria comum.
    '''
    def __init__(self, chave, valor, esquerda = None, direita = None):
        self.chave = chave
        self.valor = valor
        self.e = esquerda
        self.d = direita
    
    def _folha(self):
        '''
        método auxiliar: retorna True se o nó for uma folha e False se não for
        '''
        return self.e is None and self.d is None
    
    def __repr__(self):
        return '{}: {}'.format(self.chave, self.valor)
    
    def __str__(self):
        return self.__repr__()
    
class _3No:
    '''
    Classe auxiliar de N� Duplo (3-Node)
    Gurada dois valores e duas chaves, al�m de refer�ncias para as tr�s
    subarvores a esquerda, abaixo e a direita.
    '''
    def __init__(self, chavemin, valormin, chavemax, valormax, esquerda = None,
                 abaixo = None, direita = None):
        self.chavemin = chavemin
        self.chavemax = chavemax
        self.valormin = valormin
        self.valormax = valormax
        self.e = esquerda
        self.b = abaixo
        self.d = direita
    
    def _folha(self):
        '''
        método auxiliar: retorna True se o nó for uma folha e False se não for
        '''
        return self.e is None and self.b is None and self.d is None
    
    def __repr__(self):
        return '{}: {}, {}: {}'.format(self.chavemin, self.valormin,
                                       self.chavemax, self.valormax)
    
    def __str__(self):
        return self.__repr__()

class _4No:
    '''
    Classe auxiliar de nos triplos (4-Node) temporários.
    Guarda três chaves, três valores e quatro referências para subárvores:
    
                        (B | D | E)
                        /  /  \  \
                      (A)(C) (F)(H)
    Os parâmetros c_ são as chaves, os parâmetros v_ os valores e os parâmetros
    r_ são as referências para as subarvores.
    '''
    def __init__(self, c1, c2, c3, v1, v2, v3, r1 = None, r2 = None, r3 = None,
                 r4 = None):
        self.v1, self.v2, self.v3 = v1, v2, v3
        self.c1, self.c2, self.c3, = c1, c2, c3
        self.r1, self.r2, self.r3, self.r4 = r1, r2, r3, r4
    
    def __repr__(self):
        return "{}: {}, {}: {}, {}: {}".format(self.c1, self.v1, self.c2,
                                               self.c2, self.v3, self.c3)
    
    def __str__(self):
        return self.__repr__()

class Arvore:
    '''
    Classe Principal de �rvore Bin�ria Balanceada.
    Pode ser constru�da atrav�s de um iter�vel de tuplas.
    '''
    def __init__(self, iteravel = None):
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
    
    def inserir(self, chave, valor):
        self.raiz, aux = self.__inserir(chave, valor, self.raiz)
    
    def __inserir(self, chave, valor, no):
        if no is None:
            return _2No(chave, valor), None
        elif no._folha():
            if type(no) == _2No:
                return self.__expandir(chave, valor, no), None
            elif type(no) == _3No:
                pass
        else:
            pass
    
    def __expandir(self, chave, valor, no):
        '''
        Função auxiliar que transforma um nó simples em um nó duplo.
        '''
        if type(no) == _2No:
            cmax, cmin, vmax, vmin, e, b, d = (chave, no.chave, valor, no.valor,
                                               None, no.e, no.d)\
            if chave >= no.chave else (no.chave, chave, no.valor, valor, no.e,
                                       no.d, None)
            del no
            return _3No(cmin, vmin, cmax, vmax, e, b, d)
        elif type(no) == _3No:
            if chave > no.chavemin and chave > no.chavemax:
                c1 = no.chavemin
                v1 = no.valormin
                c2 = no.chavemax
                v2 = no.valormax
                c3 = chave
                v3 = valor
            elif chave > no.chavemin and chave < no.chavemax:
                c1 = no.chavemin
                v1 = no.valormin
                c2 = chave
                v2 = valor
                c3 = no.chavemax
                v3 = no.valormax
            else:
                c1 = chave
                v1 = valor
                c2 = no.chavemin
                v2 = no.valormin
                c3 = no.chavemax
                v3 = no.valormax