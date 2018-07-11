# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados
Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                    Created on Sun Apr  8 04:32:53 2018
                            
Descricao: Códigos da ListaDupla (classe de lista duplamente encadeada) e
da classe auxiliar Nodo.
A classe ListaDupla armazena valores em nós duplamente encadeados.
A classe Nodo contem o funcionamento dos códigos dos nós.

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
'''

#------------------------------------------------------------------------------
#              Representação de uma lista duplamente encadeada
#                         de tamanho n, onde os números
#                       representam os índices de cada nó
#
#            Primeiro
#               \/
#      None<-[Cabeça]<->[0]<->[1]<->...<->[n-1]->None
#                                          /\
#                                        Último
#
#------------------------------------------------------------------------------

class _No():
    '''
    Classe definida para os nós que farão parte da lista duplamente
    encadeada.
    '''
    def __init__(self, valor = None, anterior = None, proximo = None):
        '''
        Metodo construtor da classe Nodo.
        '''
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo
        
    def __repr__(self):
        '''
        Método para exibição de valor válido de um nodo.
        '''
        return self.valor.__repr__()
    
    def __str__(self):
        '''
        Esse método retorna o valor string do do nodo, e é chamada quando
        é necessário converter o valor do nodo para string, como na função 
        print.
        '''
        return self.valor.__str__()    
    
class Lista():
    '''
    Classe de listas duplamente encadeadas. Nessas listas, os valores a
    inseridos na lista são armazenados em nós dipostos um após o outro. Cada
    nó guarda a referência do próximo nó e do nó anterior a ele.
    '''
    def __init__(self, *elementos):
        '''
        Método construtor da lista duplamente encadeada.
        Esse método aceita parâmetro nenhum, ou um ou mais parâmetros que 
        são, em ordem, anexados a lista.
        '''
        self.primeiro = _No()
        self.ultimo = self.primeiro
        self.tamanho = 0
        for valor in elementos:
            self.anexar(valor)
    
    def anexar(self, valor):
        '''
        Esse método cria um novo nodo no final da lista e salva nele o 
        parâmetro valor.
        '''
        self.ultimo.proximo = _No(valor, self.ultimo, None)
        self.ultimo = self.ultimo.proximo
    
    def __buscarno(self, i):
        '''
        Esse método busca o nó correspondente a o indice informado como
        parâmetro.
        Buscar um nó é uma operação comum, a criação de um método separado para
        tal, visa facilitar essa tarefa.
        Esse método levanta uma exceção IndexError, caso o índice não pertença
        a lista.
        Esse é o método que busca um nó da esquerda para a direita (i >= 0)
        '''
        atual = self.primeiro.proximo
        cont = 0
        while cont < atual:
            if atual.proximo is None:
                raise IndexError("Índice fora de alcance.")
            else:
                atual = atual.proximo
                cont += 1
        return atual
    
    def __buscarnoadire(self, i):
        '''
        Método com a mesma funcionalidade do método __buscarno, com a diferença
        de realizar a busca da direita para a esquerda (i < 0).
        '''
        pass
    
    def inserir(self, index, valor):
        '''
        Essa função permite inserir valores de maneira ordenada na lista.
        O índice, para essa função, deve
        '''
        # Se a lista estiver vazia, basta anexar o elemento
        if self.primeiro == self.ultimo:
            self.anexar(valor)
        else:
            pass