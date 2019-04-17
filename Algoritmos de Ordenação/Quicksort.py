#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br
                    Created on Sun Apr 14 21:09:38 2019
Descrição: Algoritmo de ordenação Quicksort

                        Licenca: The MIT License (MIT)
                    Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

def quicksort(arr, inicio = 0, fim = -1):
    if fim == -1:
        fim = len(arr)-1
    if inicio >= fim:
        return
    pivo = esq = inicio
    dir_ = fim
    while esq < dir_:
        while dir_ > inicio:
            if arr[pivo] > arr[dir_]:
                arr[pivo], arr[dir_] = arr[dir_], arr[pivo]
                pivo = dir_
                break
            dir_ -= 1
            if dir_ <= esq: break
        while esq < fim:
            if arr[pivo] < arr[esq]:
                arr[pivo], arr[esq] = arr[esq], arr[pivo]
                pivo = esq
                break
            esq += 1
            if esq >= dir_: break
    if pivo > 0: quicksort(arr, inicio, pivo-1)
    quicksort(arr, pivo+1, fim)