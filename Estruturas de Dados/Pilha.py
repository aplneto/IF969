# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Tue Jul 17 15:12:04 2018
                            
Descricao: Pilhas (ou stacks) são estruturas de dados do tipo LIFO (last-in,
first-out). São um tipo especial de estrutura linear onde todas as operações de
inserção e remoção são realizadas pela mesma extremiadade, chamada TOPO. Pense,
por exemplo, em uma pilha de livros, onde o último a ser colocado na pilha é
o primeiro a ser retirado.

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

class _No:
    '''
    Classe auxiliar Nó.
    '''
    def __init__(self, valor, proximo = None):
        '''
        Para esse tipo de fila é denecessário o uso de encadeamento duplo.
        '''
        self.valor = valor
        self.proximo = proximo
    
    def __repr__(self):
        return "_No({})".format(self.valor.__repr__())
    
    def __str__(self):
        return self.valor.__str__()

class Pilha:
    '''
    Classe principal pilha. Pode ser construída vazia ou a partir de um
    iterável. É possível limitar o tamanho da fila com o uso do kwarg 'lim'.
    Na pilha, a operação de inserção é chamada de empilhar (push) e a de
    remoção de desempilhar (pop). Além dessas, também há a operação de puxar
    (pull) que move um nó para o topo da pilha.
    '''
    def __init__(self, iteravel = None, **kwargs):
        self.primeiro = None
        self.limite = kwargs.get("lim", -1)
        self.__tam = 0
        if iteravel is not None:
            for item in iteravel:
                self.empilhar(item)
    
    def empilhar(self, item):
        '''
        Numa pilha a inserção (ou empilhamento) se dá sempre no início.
        '''
        if self.__tam < self.limite or self.limite == -1:
            self.primeiro = _No(item, self.primeiro)
            self.__tam += 1
        else:
            return ValueError ("pilha cheia")
    
    def desempilhar(self):
        '''
        A operação de remoção (desempilhamento) acontece sempre no primeiro
        elemento da pilha.
        '''
        if self.primeiro is None:
            raise IndexError ("pilha vazia")
        aux = self.primeiro
        self.primeiro = self.primeiro.proximo
        aux.proximo = None
        valor = aux.valor
        del aux
        self.__tam -= 1
        return valor
    
    def puxar(self, index = 1):
        '''
        A função de puxar altera a prioridade de um determinado elemento da
        pilha, colocando-o na primeira posição.
        '''
        if index <= 0:
            raise ValueError ("insira um índice válido")
        atual = self.primeiro
        cont = 1
        while cont < index:
            if atual.proximo is None:
                raise IndexError ("índice fora de alcance")
            else:
                atual = atual.proximo
            cont += 1
        aux = atual.proximo
        atual.proximo = atual.proximo.proximo
        aux.proximo = self.primeiro
        self.primeiro = aux
    
    # Os métodos abaixo são comuns entre as pilhas e as listas ou são métodos
    # especiais
    
    def __contains__(self, item):
        atual = self.primeiro
        while atual is not None:
            if atual.valor == item:
                return True
            else:
                atual = atual.proximo
        return False
    
    def __len__(self):
        """
        Ao usar o método __len__ nas listas encadeadas, o método contava os nós
        um a um. Na pilha, uma vez que armazenamos o número de nós em uma
        varíavel (self.__tam), é desnecessário realizar a contagem novamente.
        """
        return self.__tam
    
    def __getitem__(self, i):
        cont = 0
        atual = self.primeiro
        while cont < i:
            if atual.proximo is None:
                raise IndexError ("índice fora de alcance")
            else:
                atual = atual.proximo
        return atual.valor
    
    def __str__(self):
        atual = self.primeiro
        msg = ''
        while atual is not None:
            if msg: msg += ' -> '
            msg += repr(atual.valor)
            atual = atual.proximo
        return "[{}]".format(msg)
    
    def __repr__(self):
        atual = self.primeiro
        msg = ''
        while atual is not None:
            if msg: msg = ', '+msg
            msg = repr(atual.valor) + msg
            atual = atual.proximo
        return "Pilha([{0}])".format(msg)
    
    def __iter__(self):
        def _ponteiro(n):
            while n is not None:
                yield n.valor
                n = n.proximo
            raise StopIteration
        return _ponteiro(self.primeiro)