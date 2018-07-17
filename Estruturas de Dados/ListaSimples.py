# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Tue Jul 10 22:18:48 2018
                            
Descricao: Código da classe de listas simples. Também contém o código da classe
auxiliar de nós, usados na construção da lista.

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto

"""
#------------------------------------------------------------------------------
# Demonstração gráfica simples de uma lista de encadeamento simples de tamanho
# n, onde os números entre colchetes representam os índices de cada nó
#
#                Primeiro
#                  \/
#               [Cabeça] -> [0] -> [1] -> ... -> [n-1] -> None
#                                                 /\
#                                               Último
#
#------------------------------------------------------------------------------

class _No():
    '''
    Classe auxiliar nó. Guarda um valor e uma referência para o próximo nó da
    lista. Quando não há um próximo nó, a referência é None.
    item: objeto ou valor a ser guardado no nó
    prox: referência para o próximo nó
    '''
    def __init__(self, item = None, prox = None):
        self.item = item
        self.prox = prox
    
    def __repr__(self):
        return self.item.__repr__()
    
    def __str__(self):
        return self.item.__str__()

class Lista():
    '''
    Classe principal de Lista simplesmente encadeada. Os nós dessa lista
    pertencem a classe _No. Esses nós guardam referências para o nó sucessor,
    caso ele exista, ou para None, caso não haja nó sucessor.
    '''
    def __init__(self, iteravel = None):
        '''
        Método construtor da Lista.
        Esse é o método que será chamado no momento em que um objeto do tipo
        Lista for instanciado. Logo, são os parâmetros desse método que
        determinam quais parâmetros são necessários a construção do objeto.
        No caso desse método em espeífico, ele pode ser construído a partir de
        um outro iterável (como uma tupla, dicionário, lista ou string) ou pode
        ser construído como uma lista vazia.
        '''
        self.primeiro = self.ultimo = _No()
        if not iteravel is None:
            for obj in iteravel:
                self.anexar(obj)
    
    def anexar(self, item):
        '''
        Método insere um item na última posição da lista.
        '''
        self.ultimo.prox = _No(item)
        self.ultimo = self.ultimo.prox
    
    def inserir(self, index, item):
        '''
        Método usado para inserir um item numa posição específica da lista,
        colocando todos os itens subsequentes uma posição para a direita.
        Caso o indice dado seja maior que o indíce do último elemento da lista,
        o item é inserido na última posição.
        '''
        atual = self.primeiro
        cont = 0
        while cont < index and atual.prox is not None:
            atual = atual.prox
            cont += 1
        atual.prox = _No(item, atual.prox)
        # A próxima linha verifica se o novo nó foi inserido na última posição
        # da lista
        if atual.prox.prox is None:
            self.ultimo = atual.prox
    
    def modificar(self, index, item):
        '''
        Método usado para modificar valor de um nó existente na lista.
        Caso o nó não exista na lista, o método levanta uma exceção IndexError.
        '''
        if self.primeiro == self.ultimo:
            raise IndexError ("lista vazia")
        atual = self.primeiro
        cont = -1
        while cont < index:
            if atual.prox is None:
                raise IndexError ("índice fora de alcance")
            else:
                atual = atual.prox
                cont += 1
        atual.item = item
    
    def buscar(self, index):
        '''
        Método usado para acessar um elemento da lista através de seu índice.
        Caso o índice não pertença a lista, uma exceção IndexError é levantada.
        Esse método faz a busca da esquerda para a direita (indice >= 0)
        '''
        atual = self.primeiro
        cont = -1
        while cont < index:
            if atual.prox is None:
                raise IndexError ("índice fora de alcance")
            else:
                atual = atual.prox
                cont += 1
        return atual.item
    
    def indice(self, item, inicio = None, fim = None):
        '''
        Método usado para encontrar o índice dado um elemento da lista. Esse
        método retorna o índice da primeira posição em que o elemento aparece,
        caso ele apareça mais de uma vez na mesma lista.
        É possível limitar a busca a um determinado intervalo da lista
        informando os parametros inicio e fim.
        Caso o item não pertença a lista, uma exceção ValueError é levantada.
        '''
        if inicio is not None and not isinstance(inicio, int):
            raise ValueError ("inicio deve ser um número inteiro")
        elif fim is not None and not isinstance(fim, int):
            raise ValueError ("fim deve ser um número inteiro")
        else:
            if inicio is None:
                inicio = 0
            if fim is None:
                fim = float('inf')
        atual = self.primeiro
        cont = 0
        while atual.prox is not None:
            if atual.prox.item == item and (cont >= inicio and cont <= fim):
                return cont
            else:
                atual = atual.prox
                cont += 1
        raise ValueError ("{} não pertencem a lista".format(repr(item)))
    
    def retirar(self, index = 0):
        '''
        Método usado para remover um nó da lista e recuperar o valor que o nó
        guardava.
        Equivalente ao método .pop das listas nativas de Python.
        '''
        # Se a lista estiver vazia o método levanta uma exceção IndexError
        if self.primeiro == self.ultimo:
            raise IndexError ("não é possível retirar valores de lista vazia")
        atual = self.primeiro
        cont = 0
        while cont < index:
            if atual.prox is None:
                raise IndexError("índice fora de alcance")
            else:
                atual = atual.prox
                cont += 1
        aux = atual.prox
        atual.prox = aux.prox
        aux.prox = None
        # Se o nó que estiver para ser deletado for o último, o último então
        # passa a ser o nó anterior a ele
        if self.ultimo == aux:
            self.ultimo = atual
        valor = aux.item
        del aux
        return valor
    
    def remover(self, item):
        '''
        Método usaod para remover um determinado nó que contenha um item
        específico.
        Caso não o item informado não esteja na lista, o método levanta uma
        exceção ValueError.
        '''
        # Se a lista estiver vazia o método levanta uma exceção ValueError
        if self.primeiro == self.ultimo:
            raise ValueError ("não é possível remover itens de uma lista vazia")
        anterior = self.primeiro
        atual = anterior.prox
        while not atual is None and atual.item != item:
            anterior = atual
            atual = anterior.prox
        if atual is None:
            raise ValueError("{} não pertence a lista".format(repr(item)))
        else:
            anterior.prox = atual.prox
            atual.prox = None
            if self.ultimo == atual:
                self.ultimo = anterior
            del atual
    
    # Adiante estão os métodos especiais (magic operators) de Python.
    # Note que alguns deles apenas chamam funções criadas anteriormente
    
    def __contains__(self, item):
        '''
        Método usado para verificar se um determinado item pertence ou não a
        lista.
        Esse é o método utilizado quando o operador in é chamado. Deve retornar
        True caso o objeto pertença a lista e False caso contrário.
        '''
        if self.primeiro == self.ultimo:
            return False
        atual = self.primeiro.prox
        while atual is not None:
            if atual.item == item:
                return True
            else:
                atual = atual.prox
        return False
    
    def __len__(self):
        '''
        Esse é o método que retorna o tamanho de uma lista.
        Nessa implementação em específico, o método conta quantos nós fazem
        parte da lista.
        '''
        no = self.primeiro.prox
        cont = 0
        while no is not None:
            cont += 1
            no = no.prox
        return cont
    
    def __str__(self):
        '''
        Método de conversão do objeto para string. Esse é o método chamado, por
        exemplo, quando se usa a função print(obj)
        '''
        string = ''
        anterior = self.primeiro
        atual = anterior.prox
        while not atual is None:
            string += atual.item.__repr__()
            if atual.prox is not None:
                string += ', '
            anterior = atual
            atual = anterior.prox
        return "[{}]".format(string)
    
    def __repr__(self):
        '''
        Método usado para se obter uma representação válida de um objeto. Esse
        é o método chamado quando, por exemplo, você digita o nome de um objeto
        ou variável no console e recebe como output uma string contendo uma
        representação do valor do objeto.
        '''
        return self.__str__()
    
    def __getitem__(self, i):
        '''
        Método usado para se obter um objeto através do acesso direto por
        índice. Por exemplo:
            Em uma lista com o seguinte valor: ['abc', 123, True, inf], o
            método __getitem__ permite se obter os valores dos elementos a
            partir de seus índices.
            
            In: lista[0]
            Out: 'abc'
            
            In: lista[1]
            Out: 123
            
            ...e assim sucessivamente....
        '''
        return self.buscar(i)
    
    def __setitem__(self, index, item):
        '''
        Esse método funciona de forma similar ao método __getitem__, mas ao
        invés de retornar o valor desejado, ele muda o valor do elemento na
        posição específicada.
        '''
        self.modificar(index, item)
    
    def __iter__(self):
        '''
        Método usado para retornar um iterador (objeto do tipo iter) do objeto.
        Esse método permite a iteração através do for.
        '''
        self.__atual = self.primeiro.prox
        return self
    
    def __next__(self):
        '''
        Define o comportamento do iterador do objeto.
        O fim da iteração é marcado com o levantamento da exceção StopIteration
        '''
        if self.__atual is None:
            raise StopIteration
        else:
            item = self.__atual.item
            self.__atual = self.__atual.prox
            return item
