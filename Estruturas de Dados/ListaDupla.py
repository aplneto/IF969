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

class Nodo():
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

class ListaDupla():
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
        self.primeiro = Nodo()
        self.ultimo = self.primeiro
        self.tamanho = 0
        for valor in elementos:
            self.anexar(valor)
    
    def anexar(self, valor):
        '''
        Esse método cria um novo nodo no final da lista e salva nele o 
        parâmetro valor.
        '''
        self.ultimo.proximo = Nodo(valor, self.ultimo, None)
        self.ultimo = self.ultimo.proximo
        self.tamanho += 1
        return
    
    def inserir(self, valor, chave):
        '''
        Essa função permite inserir valores de maneira ordenada na lista.
        '''
        if (chave >= self.tamanho):
        # Se a chave for maior ou igual ao tamanho da lista, a inserção é no
        # final, já que o último elemento da lista tem índice self.tamanho-1
            self.anexar(valor)
        else:
            nodo = self.__buscar_nodo(chave)
            nodo.anterior = Nodo(valor, nodo.anterior, nodo)
            nodo.anterior.anterior.proximo = nodo.anterior
            self.tamanho += 1
            return
    
    def remover(self, key = -1):
        '''
        Esse método remove um nodo da lista e retorna para o usuário o 
        valor armazenado. A busca é feita pelo índice do nodo.
        O nodo retornado pode ser informado como parâmetro,
        mas é, por padrão, sempre o último.
        '''
        nodo = self.__buscar_nodo(key)
        if (nodo == self.primeiro.proximo):
        # Se for o nodo for o primeiro a ser removido, chamar o método de 
        # remoção do nodo no início é mais simples.
            return self.__removerinicio(nodo)
        elif (nodo == self.ultimo):
        # Se o nodo for o último, é chamado o método de remoção do final
            return self.__removerfinal(nodo)
        else:
        # Esse é o procedimento de remoção de um nodo que não é o primeiro ou o
        # último
            nodo.proximo.anterior = nodo.anterior
            nodo.anterior.proximo = nodo.proximo
            nodo.proximo = nodo.anterior = None
            valor = nodo.valor
            del nodo
            self.tamanho -= 1
            return valor
    
    def __removerinicio(self, nodo):
        '''
        Esse método remove o primeiro nodo de uma lista e retorna para o
        usuário o valor guardado nele.
        A verificação se a lista é vazia acontece na função de busca.
        '''
        self.primeiro.proximo = nodo.proximo
        if (nodo.proximo is None):
        # Se o proximo nodo não existir, então essa é a remoção do último nodo
            self.ultimo = nodo.anterior
        else:
        # Se não for o último, a informação no próximo nodo deve ser modificada
            nodo.proximo.anterior = nodo.anterior
            nodo.proximo = None
        nodo.anterior = None
        valor = nodo.valor
        del nodo
        self.tamanho -= 1
        return valor
    
    def __removerfinal(self, nodo):
        '''
        Método chamado quando a remção a ser executada é a do último nodo
        da lista.
        Novamente, a verificação do tamanho da lista acontece na função de
        busca.
        '''
        nodo.anterior.proximo = nodo.proximo
        self.ultimo = nodo.anterior
        nodo.anterior = None
        valor = nodo.valor
        del nodo
        self.tamanho -= 1
        return valor
    
    def indice(self, item):
        '''
        Método que realiza a busca de um item na lista e, quando o encontra
        retorna o índice desse item.
        Se houverem mais de um do item na lista, o índice retornado é sempre o
        primeiro
        '''
        itr = self.__iter__()
        achou = False
        cont = 0
        try:
            while not achou:
                if (item == next(itr)):
                    achou = True
                else:
                    cont += 1
        except StopIteration:
            raise ValueError (item.__repr__() + " não está na lista")
        return cont

    def __buscar_nodo(self, key):
        '''
        Método que busca um nodo de índice específico.
        '''
        if (type(key) != int):
            raise TypeError ("Índices devem ser inteiros")
        elif (self.tamanho == 0):
            raise IndexError ("Lista Vazia")
        elif ((key >= self.tamanho) or (key<-self.tamanho)):
        # O último índice da lista é sempre o tamanho da lista -1
        # Assim como, regressivamente, o primeiro é igual a -1*tamanho da lista
            raise IndexError ("Índice inexistente")
        elif (key <0):
            key += self.tamanho
        cont = 0
        node = self.primeiro
        while cont<=key:
            node = node.proximo
            cont += 1
        return node

    def comparar(self, item1, item2):
        if item1 > item2:
            return 1
        elif item1 == item2:
            return 0
        else:
            return -1

    def __repr__ (self):
        '''
        Método definido para a exibição válida do objeto lista
        '''
        string = '['
        cont = 1
        for elemento in self:
            string += elemento.__repr__()
            if (cont < self.tamanho):
            # Para diferenciar essa de uma lista padrão de Python, o separador
            # escolhido foi o dois pontos ';'
                string += '; '
            cont += 1
        string += ']'
        return string
    
    def __len__(self):
        '''
        Retorna o tamanho da lista.
        '''
        return self.tamanho
    
    def __iter__(self):
        self.__atual = self.primeiro.proximo
        return self
    
    def __next__(self):
        if self.__atual is None:
            raise StopIteration
        valor = self.__atual.valor
        self.__atual = self.__atual.proximo
        return valor
    
    def __getitem__(self, key):
        '''
        Esse Método permite o resgate de valores dentro da lista com a 
        utilização de um índice no formato instancia[key]
        '''
        return self.__buscar_nodo(key).valor
    
    def __setitem__(self, key, value):
        '''
        Méotodo usado para modificar o valor de um novo através de índice.
        '''
        nodo = self.__buscar_nodo(key)
        nodo.valor = value
        return
    
    def __contains__ (self, valor):
        '''
        Método usado para buscar determinado elemento dentro da lista.
        '''
        itr = self.__iter__()
        achou = False
        try:
            while not achou:
                if (valor == next(itr)):
                    achou = True
        except StopIteration:
            return achou
        return achou
    
    def __add__(self, outra):
        '''
        Método usado para somar duas listas.
        '''
        newlist = ListaDupla()
        for item in self:
            newlist.anexar(item)
        for item in outra:
            newlist.anexar(item)
        return newlist