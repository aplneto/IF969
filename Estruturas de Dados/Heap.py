#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br
                    Created on Sat Apr 13 14:43:16 2019
Descrição: Estruturas de Heap Máximo e Mínimo

                        Licenca: The MIT License (MIT)
                    Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

import numpy

class Heap:
    '''Superclasse Heap
    
    Essa classe é o molde tanto para heap máximo quanto para heap mínimo.
    
    Alguns métodos são implementados de igualmente tanto para o heap máximo
    quanto para o heap mínimo. Para evitar a redundância de código, os métodos
    compartilhados entre as duas classes estão implementados aqui.
    '''
    
    pai = lambda i: i//2
    filho_esq = lambda i: i*2
    filho_dir = lambda i: (i*2)+1
    
    def __init__(self, tam = -1, arr = None, **kwargs):
        '''Método construtor do heap
        
        Args:
            tam (int): tamanho do heap. Quando não fornecido, o parâmetro arr
                se torna obrigatório.
            arr (iterável): parâmetro opcional, array sobre o qual o heap
                pode ser construído. Se o array for maior que o tamanho do
                heap, os últimos elementos além do tamanho serão ignorados.
        Kwargs:
            key_type (class): tipo de objeto a ser usado como chave.
        '''
        if tam == 0 :
            raise ValueError ("Heap de tamanho 0")
        if tam == -1:
            if not arr: raise ValueError("arr ou tam devem ser fornecidos")
            tam = len(arr)
            
        self.tam = 0
        self.heap = numpy.full(tam+1, -1,
                                    dtype = kwargs.get('key_type', int))
        if arr:
            menor = len(arr)
            if tam < menor: menor = tam
            for i in range(menor):
                self.heap[i+1] = arr[i]
                self.tam += 1
            self.heapify()

    def heapify(self):
        e = self.tam//2
        while e >= 1:
            self.heapify_down(e)
            e -= 1

    def heapify_down(self, i):
        raise NotImplemented
    
    def heapify_up(self, i):
        raise NotImplemented
    
    def heap_sort(self):
        '''Esse método ordena o vetor interno
        
        Warnings:
            O heapsort é um método destrutivo, ao ordenar o vetor interno
                você quebra a propriedade do Heap.
            Esse método assume que o vetor interno representa um heap válido.
                Veja o método 'is_heap' para mais informações.
        '''
        lim = self.tam
        while self.tam > 1:
            self.heap[1], self.heap[self.tam] = self.heap[self.tam], self.heap[1]
            self.tam -= 1
            self.heapify_down(1)
        self.tam -=1
        return self.heap[1:lim+1]
            
    def inserir(self, n):
        if self.tam +1 == self.heap.size: raise RuntimeError ("Heap cheio")
        self.tam += 1
        self.heap[self.tam] = n
        self.heapify_up(self.tam)
    
    def maximo(self):
        if self.is_empty: raise RuntimeError("Heap vazio")
        self.heap[1], self.heap[self.tam] = self.heap[self.tam], self.heap[1]
        valor = self.heap[self.tam]
        self.heap[self.tam] = -1
        self.tam -=1
        self.heapify_down(1)
        return valor
    
    def remover(self, i):
        '''Método de remoção ordenadao
        
        remove um valor do heap de acordo com índice, sendo 1 a raiz do heap
        
        Args:
            i (int): indice a ser removido
        '''
        if i <= 0: raise IndexError(i)
        if i == 1: return self.maximo()
        self.heap[i], self.heap[self.tam] =  self.heap[self.tam], self.heap[i]
        valor = self.heap[self.tam]
        self.heap[self.tam] = -1
        self.tam -= 1
        if self.heap[i] > self.heap[Heap.pai(i)]: self.heapify_up(i)
        else: self.heapify_down(i)
        return valor

    @property
    def is_empty(self):
        return self.tam == 0
    
    @property
    def is_heap(self):
        """Esse método verifica se a propriedade do heap é válida
        """
        raise NotImplemented
    
    def __len__(self):
        return self.tam
    
    def __str__(self):
        return "{}".format(' '.join(str(x) for x in self.heap[1:self.tam+1]))
    
    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__,
                self.heap.size-1, self.heap[1:self.tam+1].__repr__(),
         'dtype = ' + self.heap.dtype.__str__().__repr__())
    
    def __getitem__(self, index):
        if self.is_empty:
            raise IndexError("Heap vazio")
        elif index > self.tam or index < 1:
            raise IndexError(index)
        return self.heap[index]
    
class HeapMax(Heap):
    def __init__(self, tam = -1, arr = None, **kwargs):
        '''Método construtor do heap máximo
        
        Args:
            tam: tamanho do heap
            arr (None): array ou iterável a partir do qual o heap vai ser
                construído.
        Kwargs:
            key_type (int): método que determina o tipo de objeto a ser usado
                como chave.
        '''
        Heap.__init__(self, tam, arr, **kwargs)
    
    def heapify_down(self, i):
        '''Método de filtragem para baixo
        '''
        filho = Heap.filho_esq(i)
        while filho <= self.tam:
            d = Heap.filho_dir(i)
            if d <= self.tam and self.heap[d] > self.heap[filho]:
                filho = d
            if self.heap[i] >= self.heap[filho]: break
            self.heap[i], self.heap[filho] = self.heap[filho], self.heap[i]
            i = filho
            filho = Heap.filho_esq(i)
    
    def heapify_up(self, i):
        '''Método de filtragem para cima
        '''
        while i > 1:
            pai = Heap.pai(i)
            if self.heap[i] < self.heap[pai]: break
            self.heap[pai], self.heap[i] = self.heap[i], self.heap[pai]
            i = pai
    
    @property
    def is_heap(self):
        i = self.tam
        while i > 1:
            if self.heap[i] > self.heap[Heap.pai(i)]: return False
            i -= 1
        return True

class HeapMin(Heap):
    def __init__(self, tam = -1, arr = None, **kwargs):
        '''Método construtor do Heap mínimo
        
        Args:
            tam: tamanho do heap
            arr (None): array ou iterável a partir do qual o heap vai ser
                construído.
        Kwargs:
            key_type (int): método que determina o tipo de objeto a ser usado
                como chave.
        '''
        Heap.__init__(self, tam, arr, **kwargs)
    
    def heapify_down(self, i):
        '''Método de filtragem para baixo
        '''
        filho = Heap.filho_esq(i)
        while filho <= self.tam:
            d = Heap.filho_dir(i)
            if d <= self.tam and self.heap[d] < self.heap[filho]:
                filho = d
            if self.heap[i] <= self.heap[filho]: break
            self.heap[i], self.heap[filho] = self.heap[filho], self.heap[i]
            i = filho
            filho = Heap.filho_esq(i)
    
    def heapify_up(self, i):
        '''Método de filtragem para cima
        '''
        while i > 1:
            pai = Heap.pai(i)
            if self.heap[i] > self.heap[pai]: break
            self.heap[pai], self.heap[i] = self.heap[i], self.heap[pai]
            i = pai
    
    @property
    def is_heap(self):
        i = self.tam
        while i > 1:
            if self.heap[i] < self.heap[Heap.pai(i)]: return False
            i -= 1
        return True