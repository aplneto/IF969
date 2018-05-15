# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sun May  6 01:18:16 2018

Descrição: Classe auxiliar usada para cronometrar algoritmos em
testes de performance.

Licenca: The MIT License (MIT)
                    Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

import time

class Cronometro:
    def __init__(self):
        self.__tempo = 0
        self.__correndo = False
    
    def iniciar(self):
        self.__inicio = time.clock()
        self.__correndo = True
    
    def parar(self):
        self.__tempo += time.clock() - self.__inicio
        self.__correndo = False
    
    def zerar(self):
        self.__tempo = 0

    def __repr__(self):
        return 'Cronômetro {0}: '.format('correndo' if self.__correndo \
                           else 'parado')+self.__str__()

    def __str__(self):
        if self.__correndo:
            self.__tempo = time.clock() - self.__inicio
        return '{0: .2f} s'.format(self.__tempo)
    
    def __getattr__(self, attr):
        if attr == 'tempo':
            return self.__str__()