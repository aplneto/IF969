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
        return "_No({})".format(self.valor.__repr__())
    
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
    def __init__(self, iteravel = None):
        '''
        Método construtor da lista duplamente encadeada.
        É possível construir uma lista duplamente encadeada apartir de um
        iterável passado como parâmetro para esse método.
        '''
        self.primeiro = self.ultimo = _No()
        if not iteravel is None:
            for obj in iteravel:
                self.anexar(obj)
    
    def anexar(self, valor):
        '''
        Esse método cria um novo nodo no final da lista e salva nele o 
        parâmetro valor.
        '''
        self.ultimo.proximo = _No(valor, self.ultimo, None)
        self.ultimo = self.ultimo.proximo
    
    def __buscarno(self, i):
        '''
        Esse método busca o e retorna o nó correspondente ao indice 
        informado como parâmetro, levantando uma exceção IndexError, caso o
        índice não pertença a lista.
        Esse método é útil pois a mesma operação se repete em dois métodos
        distintos (buscar e modificar).
        Esse método é um pouco mais complicado do que o método de busca da
        lista simples porque a busca pode ser feito da esquerda para a direita
        (i >= 0) ou da direita para a esquerda (i < 0). Para isso são
        necessários alguns cálculos antes.
        '''
        if self.primeiro == self.ultimo:
            raise IndexError ("lista vazia")
        if i >= 0:
            # Se o índice for positivo a lista anda da esquerda para a direita,
            # começando do primeiro nó
            atual = self.primeiro
            passo = lambda no: no.proximo
            comp = lambda n, i: n<i
            inc = lambda n: n+1
        else:
            # Caso o índice seja negativo a lista anda da direita para a
            # esquerda, começando do último nó
            atual = self.ultimo
            passo = lambda no: no.anterior
            comp = lambda n, i: n>i
            inc = lambda n: n-1
        cont = -1
        while comp(cont, i):
            if passo(atual) is None or passo(atual) == self.primeiro:
                raise IndexError ("índice fora de alcance")
            atual = passo(atual)
            cont = inc(cont)
        return atual
    
    def buscar(self, index):
        '''
        Método para buscar o valor guardado pelo nó de índice informado como
        parâmetro. Levanta uma exceção IndexError caso o índice não pertença a
        lista.
        Código da busca no método __buscarno
        '''
        return self.__buscarno(index).valor
    
    def modificar(self, index, valor):
        '''
        Função semelhante a de busca, no entanto, encontra um nó específico
        e modifica o valor armazenado naquele nó.
        '''
        no = self.__buscarno(index)
        no.valor = valor
        
    def inserir(self, index, valor):
        '''
        Esse método permite inserir valores de maneira ordenada na lista.
        Caso o índice seja muito maior do que o tamanho da lista, o valor é
        inserido no final, e caso seja muito menor o valor será inserido no
        início.
        '''
        # Se a lista estiver vazia, basta anexar o elemento
        if self.primeiro == self.ultimo:
            self.anexar(valor)
        else:
            if index >= 0:
                passo = lambda no: no.proximo
                atual = self.primeiro
            else:
                passo = lambda no: no.anterior
                atual = self.ultimo
            cont = 0
            while cont < abs(index) and passo(atual) is not None:
                atual = passo(atual)
                cont += 1
            atual.proximo = _No(valor, atual, atual.proximo)
            if self.ultimo == atual:
                self.utlimo = atual.proximo
            else:
                atual.proximo.anterior = atual.proximo
    
    def indice(self, valor, inicio = None, fim = None):
        '''
        Esse método busca pelo índice de um valor na lista. Ele retorna o
        índice da primeira posição em que o valor aparece (caso o valor apareça
        mais de uma vez na lista) ou levanta uma exceção ValueError, caso o
        valor não pertença a nenhum dos nós da lista.
        '''
        if inicio is not None and not isinstance (inicio, int):
            raise ValueError ("parâmetro inicio deve ser um número inteiro")
        elif fim is not None and not isinstance (fim, int):
            raise ValueError ("parâmetro fim deve ser um número inteiro")
        else:
            if inicio is None:
                inicio = 0
            if fim is None:
                fim = float('inf')
        atual = self.primeiro
        cont = 0
        while atual.proximo is not None:
            if atual.proximo.valor == valor and\
            (cont >= inicio and cont <= fim):
                return cont
            else:
                atual = atual.proximo
                cont += 1
        raise ValueError ('{} não está na lista'.format(repr(valor)))
    
    def retirar(self, index = 0):
        '''
        Método usado para remover um nó da lista e retornar o valor nele
        armazenado.
        '''
        if self.primeiro == self.ultimo:
            raise IndexError ("impossível retirar de lista vazia")
        no = self.__buscarno(index)
        if no == self.ultimo:
            return self.removerfim()
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior
            no.anterior = no.proximo = None
            valor = no.valor
            del no
            return valor
    
    def removerfim(self):
        '''
        Método usado para remover o último elemento da lista.
        '''
        aux = self.ultimo
        self.ultimo = aux.anterior
        aux.anterior.proximo = None
        aux.anterior = None
        valor = aux.valor
        del aux
        return valor
    
    def remover(self, valor):
        '''
        Método usado para encontrar o nó que armazena um determinado valor e
        removê-lo da lista.
        Caso o valor não exista na lista uma exceção ValueError é levantada.
        '''
        if self.primeiro == self.ultimo:
            raise ValueError ("impossível remover itens de uma lista vaiza")
        atual = self.primeiro.proximo
        while atual.valor != valor:
            if atual.proximo is None:
                raise ValueError ("{} não está na lista")
            else:
                atual = atual.proximo
        atual.anterior.proximo = atual.proximo
        if atual != self.ultimo:
            atual.proximo.anterior = atual.anterior
        else:
            self.utlimo = atual.anterior
        atual.anterior = atual.proximo = None
        del atual

    # Adiante estão os métodos especiais (magic operators) de Python.
    # Note que alguns deles apenas chamam funções criadas anteriormente
    # Para uma explicação mais detalhada dos métodos abaixo, veja o arquivo
    # ListaSimples.py
    
    def __delitem__(self, index):
        if self.primeiro == self.ultimo:
            raise IndexError ("impossível retirar de lista vazia")
        no = self.__buscarno(index)
        if no == self.ultimo:
            return self.removerfim()
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior
            no.anterior = no.proximo = None
            del no
    
    def __contains__(self, valor):
        if self.primeiro == self.ultimo:
            return False
        atual = self.primeiro.proximo
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
    
    def __len__(self):
        atual = self.primeiro.proximo
        cont = 0
        while atual is not None:
            cont += 1
            atual = atual.proximo
        return cont
    
    def __getitem__(self, i):
        return self.buscar(i)
    
    def __setitem__(self, i, v):
        self.modificar(i, v)
    
    def __str__(self):
        string = ''
        anterior = self.primeiro
        atual = anterior.proximo
        while not atual is None:
            string += atual.valor.__repr__()
            if atual.proximo is not None:
                string += ', '
            anterior = atual
            atual = anterior.proximo
        return "[{}]".format(string)
    
    def __repr__(self):
        return "Lista({0})".format(self.__str__())
    
    def __iter__(self):
        '''
        Objetos geradores também são iteráveis e, por isso, podem servir
        como iteradores de uma classe, uma vez que o método next é inerente
        a um gerador.
        '''
        def _ponteiro(p):
            while p is not None:
                yield p.valor
                p = p.proximo
            raise StopIteration
        
        return _ponteiro(self.primeiro.proximo)
