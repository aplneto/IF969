# -*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Fri Jul 13 14:02:20 2018
                            
Descricao: Árvore Binária

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
"""

#==============================================================================
#
#   Representação gráfica simples de uma árvore binária, onde as chaves são
# números inteiros e os valores são as strings contendo os números ecritos por
#                                     extenso
#
#
#                                   (5, "cinco")
#                                    /        \
#                         (4, "quatro")      (10, "dez")
#                          /      \            /      \
#                  (2, "dois")   None    (6, "seis") None
#                    /     \              /       \
#              (1, "um") (3, "três")  None (7, "oito")
#                /   \     /     \           /      \
#             None  None None  None        None   (9, "nove")
#                                                   /      \
#                                             (8, "oito)   None
#                                               /    \
#                                             None  None
#
#==============================================================================

class _No:
    '''
    Classe auxiliar nó.
    Guarda a chave, o valor e dois filhos (menores a esquerda e maiores a
    direita).
    '''
    def __init__(self, chave, valor, esquerda = None, direita = None):
        self.valor = valor
        self.chave = chave
        self.e = esquerda
        self.d = direita
    
    def __str__(self):
        return "{}:{}".format(self.chave.__repr__(), self.valor.__repr__())
    
    def __repr__(self):
        return self.__str__()

class Arvore:
    '''
    Classe principal de árvore Binária.
    Essa classe se comporta como um dicionário de Python, desde que os valores
    fornecidos como chave possam ser comparados entre si.
    A árvore pode ser construída vazia ou através de um iterável contendo
    pares, como por exemplo uma lista de tuplas onde cada tupla é composta por
    chave como elemento 0 e valor como elemento 1.
    '''
    def __init__(self, iteravel = None):
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
    
    def inserir(self, chave, valor):
        '''
        O método de inserção precisa ser recursivo, logo, precisa receber
        também qual o primeiro nóe em que o valor será inserido. Por isso, para
        facilitar o trabalho do usuário, criamos um método para chamar o
        verdadeiro método de inserção, que é uma função privada.
        '''
        self.raiz = self.__inserir(self.raiz, chave, valor)
    
    def __inserir(self, no, chave, valor):
        '''
        Note que essa função só instancia um novo nó quando encontra um nó que
        não tenha valor (no == None). Até lá, depois da chamada de recursão, a
        função sempre retorna o nó atual.
        '''
        if no is None:
            return _No(chave, valor)
        elif chave > no.chave:
            no.d = self.__inserir(no.d, chave, valor)
        elif chave < no.chave:
            no.e = self.__inserir(no.e, chave, valor)
        else:
            no.valor = valor
        return no
    
    def buscar(self, chave):
        '''
        Função de pesquisa. Recebe como parâmetro a chave de um nó e retorna o
        valor que esse nó guarda. Caso não a chave não exista, levanta uma
        exceção KeyError
        '''
        no = self.raiz
        while no is not None:
            if chave == no.chave:
                return no.valor
            elif chave < no.chave:
                no = no.e
            else:
                no = no.d
        raise KeyError (chave)
    
    def remover(self, chave):
        '''
        Existem três possibilidades de eventos quando se tenta remover um nó de
        uma árvore binária.
        Na primeira o nó buscado não existe. Nesse caso não há nada a se fazer
        se não levantar um erro.
        Na segunda, o nó buscado possui um ou nenhum filho. Nesse caso, caso o
        nó possua apenas um filho, depois de removê-lo basta promover o filho a
        posição a qual o nó estava.
        O problema surge quando o nó possui dois filhos. Nesse caso, é preciso
        uma maior cautela ao escolher o nó a ser promovido (veja a função
        __sucessor).
        '''
        self.raiz, valor = self.__remover(self.raiz, chave)
        return valor
    
    def __remover(self, nodo, chave):
        if nodo is None:
            raise KeyError(chave)
        elif chave == nodo.chave:
            valor = nodo.valor
            if nodo.d is None:
                aux = nodo
                nodo = nodo.e
                del aux
            elif nodo.e is None:
                aux = nodo
                nodo = nodo.d
                del aux
            else:
                nodo.d = self.__sucessor(nodo, nodo.d)
            return nodo, valor
    
    def __sucessor(self, no, nodo):
        '''
        Para promover um nó é necessário achar um entre os dois valor possíveis
        para a substituição: o nó imediatamente anterior ao nó que vai ser
        substituído (antecessor) ou o imediatamente posterior (sucessor). Para
        essa implementação eu escolhi fazer a substituição pelo sucessor, mas
        a implementação com o antecessor pode ser vista nos slides do professor
        Renato.
        O antecessor é sempre o maior entre os menores (o mais a direita entre
        os nós a esquerda do nó que será substituído) e o sucessor é o menor
        entre os maiores (o mais a esquerda dos nós a direita).
        '''
        if nodo.e is not None:
            nodo.e = self.__sucessor(no, nodo.e)
        else:
            aux = nodo
            no.valor = nodo.valor
            no.chave = nodo.chave
            nodo = nodo.d
            del aux
        return nodo
    
    def __contar(self, n):
        '''
        Método de contagem simples.
        '''
        if not n is None:
            return self.__contar(n.e)+self.__contar(n.d)+1
        else:
            return 0
    
    def em_ordem(self, nodo):
        '''
        Método de impressão ordenada de uma árvore binária.
        Imprime primeiro a sub-árvore da esquerda, depois a raiz e por último a
        sub-árvore da direita.
        '''
        msg = ''
        if nodo is not None:
            
            # Essa variável auxiliar serve para a colocação correta da vírgula
            aux = self.em_ordem(nodo.e)
            msg += aux
            if aux: msg += ', '
            msg += str(nodo)
            
            # Essa variável auxiliar também
            aux = self.em_ordem(nodo.d)
            if aux: msg += ', '
            msg += aux
        return msg
    
    def pre_ordem(self, nodo):
        '''
        Método de impressão em pré-ordem de uma árvore binaria.
        Imprime primeiro a raiz, depois a sub-árvore da esquerda e por último a
        sub-árvore da direita.
        '''
        msg = ''
        if nodo is not None:
            msg += str(nodo)
            aux = self.pre_ordem(nodo.e)
            if aux: msg += ', '
            msg += aux
            aux = self.pre_ordem(nodo.d)
            if aux: msg += ', '
            msg += aux
        return msg
    
    def pos_ordem(self, nodo):
        '''
        Método de impressão em pós-ordem de uma árvore binária.
        Imprime primeiro a sub-árvore da esquerda, depois a sub-árvore da
        direita e por último a raiz.
        '''
        msg = ''
        if nodo is not None:
            aux = self.pos_ordem(nodo.d)
            msg += aux
            if aux: msg += ', '
            aux = self.pos_ordem(nodo.e)
            msg += aux
            if aux: msg += ', '
            msg += str(nodo)
        return msg
    
    def chaves(self):
        '''
        Método de dicionários (dict.keys()) que retorna uma lista contendo
        todas as chaves do dicionário.
        '''
        info = []
        info = self.__chaves(self.raiz, info)
        return info
    
    def __chaves(self, nodo, chaves = []):
        if nodo is not None:
            chaves.append(nodo.chave)
            chaves = self.__chaves(nodo.e, chaves)
            chaves = self.__chaves(nodo.d, chaves)
        return chaves
    
    def valores(self):
        '''
        Método de dicionários que retorna uma lista contendo todos os valores
        do dicionário.
        '''
        info = []
        info = self.__valores(self.raiz, info)
        return info
    
    def __valores(self, nodo, valores = []):
        if nodo is not None:
            valores.append(nodo.valor)
            valores = self.__valores(nodo.e, valores)
            valores = self.__valores(nodo.d, valores)
        return valores
        
    
    # Métodos Especiais
    
    def __len__(self):
        return self.__contar(self.raiz)
    
    def __getitem__(self, chave):
        return self.buscar(chave)
    
    def __setitem__(self, chave, valor):
        return self.inserir(chave, valor)        
    
    def __str__(self):
        return "{"+self.pre_ordem(self.raiz)+"}"
    
    def __repr__(self):
        return "{"+self.em_ordem(self.raiz)+"}"
    
    # ATENÇÃO! Os métodos espeiciais abaixo são um pouco mais complexos do que
    # os métodos estudados até agora. Para aqueles que tiverem curiosidade do
    # funcionamento dos métodos a seguir, procurem por "generators and
    # coroutines"
    
    def __iter__(self):
        '''
        Usar um loop em um dicionário implica em varrer as chaves que indexam
        esse dicionário.
        O método mais simples para iterar através de um dicionário é retornar
        um iterador para a lista de chaves. basta usar a expressão abaixo:
        
        return iter(self.chaves())
        
        No entanto, para os mais curiosos, segue um método recursivo de
        iteração utilizando geradores.
        '''        
        def _ponteiro(no):
            if no.e:
                yield from _ponteiro(no.e)
            yield no.chave
            if no.d:
                yield from _ponteiro(no.d)
                
        return _ponteiro(self.raiz)
        

if __name__ == "__main__":
    preordem = [(5, "cinco"), (4, "quatro"), (2, "dois"), (1, "um"), (3, "tres"),
              (10, "dez"), (6, "seis"), (7, "sete"), (9, "nove"), (8, "oito")]
    teste = Arvore(preordem)