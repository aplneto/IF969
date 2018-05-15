# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sun May  6 01:40:48 2018

Descrição: algoritimos de ordenação elementar

                        Licenca: The MIT License (MIT)
                    Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

def bubblesort(vetor, tam):
    def troca(i, j):
        temp = vetor[i]
        vetor[i] = vetor[j]
        vetor[j] = temp
    
    for i in range(tam-1):
        for j in range(i+1, tam):
            if vetor[i] > vetor[j]:
                troca(i, j)

def selectionsort(vetor, tam):
    def trocar(i, j):
        temp = vetor[i]
        vetor[i] = vetor[j]
        vetor[j] = temp
    
    for i in range(tam-1):
        menor = i
        for j in range (i+1, tam):
            if vetor[j] < vetor[menor]: menor = j
        trocar(i, menor)

def insertionsort(vetor, tam):
    for i in range (1, tam):
        aux = vetor[i]
        j = i-1
        while (j >= 0) and (vetor[j] > aux):
            vetor[j+1] = vetor[j]
            j -=1
        vetor[j+1] = aux
