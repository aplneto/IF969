'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Thu Aug 2 19:38:54 2018
                            
Descricao: Árvore 2-3

                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
'''

class Arvore2_3(object):
    '''
    Classe Principal Árvore 2-3 (2-3 Tree).
    Existem muitas operações complexas a serem implementadas manualmente na
    árvore 2-3. Para simplificar essas operações, foi adotada uma construção de
    nós a partir de listas (ao invés de vetores).
    '''

    class _2No(object):
        '''
        Classe auxiliar do Nó simples.
        Armazena uma chave e um valor e, caso não seja folha, armazena
        referências para dois nós decendentes.
        '''
        def __init__(self, chave, valor, antecessor = None,
                     esquerda = None, direita = None):
            self.chave = chave
            self.valor = valor
            self.antecessor = antecessor
            self.decendentes = [esquerda, direita]
        
        def folha(self):
            '''
            Uma das características de uma árvore 2-3 é que se os nós não são
            folhas eles obrigatóriamente possuem o máximo de referências
            possíveis para nós decendentes, uma vez que a árvore é balanceada,
            por isso não é necessário checar as referências de todos os
            decendendentes. Ou todos são None ou nenhum é.
            '''
            return decendentes[0] is None
        
        def __str__(self):
            return '{}: {}'.format(self.chave, self.valor)
        
        def __repr__(self):
            return self.__str__()
        
        def __contains__(self, chave):
            return self.chave == chave
    
    class _3No(object):
        '''
        Classe auxiliar do Nó duplo.
        Armazena duas chaves e dois valores e, caso não seja folha, armazena
        referências para três nós decendentes.
        '''
        def __init__(self, chavemin, valormin, chavemax, valormax,
                     antecessor = None, esquerda = None, meio = None,
                     direita = None):
            self.chave = [chavemin, chavemax]
            self.valor = [valormin, valormax]
            self.antecessor = antecessor
            self.decendentes = [esquerda, meio, direita]
        
        def folha(self):
            return decendentes[0] is None
        
        def __str__(self):
            return '{}: {}, {}: {}'.format(self.chave[0], self.valor[0],
                                           self.chave[1], self.valor[1])
        
        def __repr__(self):
            return self.__str__()
        
        def __contains__(self, chave):
            return chave in self.chave
    
    def __init__(self, iteravel = None):
        '''
        O método construtor pode criar um dicionário a partir de um iterável de
        duplas (chave, valor), ou criar um novo objeto em branco.
        '''
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
        
    def inserir(self, chave, valor): 
        '''
        Método de inserção para o usuário.
        Recebe uma chave e um valor para ser indexado por essa chave na árvore.
        Atualiza o valor, caso a chave já exista. Caso não, insere a chave e o
        valor na árvore.
        '''
        self.raiz = self.__inserir(chave, valor, self.raiz)
    
    def __insrir(self, chave, valor, no):
        '''
        Método de inserção: atualiza os nós da árvore recursivamente, de maneira
        a encontrar a posição da chave e, inserí-la ou modificar o valor
        indexado por ela.
        '''
        if no is None:
            return _2No(chave, valor)
        elif no.folha():
            pass
        else:
            pass
