#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sun Jul  7 02:37:49 2019

Descrição: Funções para calcular o número de ouro
Proporção áurea, número de ouro, número áureo, secção áurea, proporção de ouro
é uma constante real algébrica irracional denotada pela letra grega phi, em
homenagem ao escultor Phideas, que a teria utilizado para conceber o Parthenon
com o valor arredondado a três casas decimais de 1,618.

https://pt.wikipedia.org/wiki/Propor%C3%A7%C3%A3o_%C3%A1urea

"""

def golden_number(precision:int = 0):
    '''
    Calcula o número de ouro a partir da soma de raízes de 1
    
    Args:
        precision (int): tamanho da série de raízes
    Returns:
        phi (int): número de ouro a partir da precisão fornecida
    '''
    x = 1
    for i in range(precision):
        x = (x+1)**0.5
    return x

def golden_number_div(precision:int = 0):
    '''
    Calcula o número de ouro a partir de uma série de soma de frações
    
    Args:
        precision (int): tamanho da série de frações
    Returns:
        phi (int): número de ouro a partir do nível de precisão fornecido
    '''
    x = 1
    for i in range(precision):
        x = 1 + 1/x
    return x