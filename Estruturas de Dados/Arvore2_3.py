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
    def __init__(self, iteravel = None):
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
    
    def buscar(self, chave):
        atual = self.raiz
        while not atual is None:
            if type(atual) == _2No:
                if atual.info[0] == chave:
                    return atual.info[1]
                elif chave < atual.info[0]:
                    atual = atual.prox[0]
                else:
                    atual = atual.prox[1]
            elif type(atual) == _3No:
                if atual.info[0][0] == chave:
                    return atual.info[0][1]
                elif atual.info[1][0] == chave:
                    return atual.info[1][1]
                elif chave < atual.info[0][0]:
                    atual = atual.prox[0]
                elif chave < atual.info[1][0]:
                    atual = atual.prox[1]
                else:
                    atual = atual.prox[2]
        raise KeyError(chave)
    
    def inserir(self, chave, valor):
        self.raiz = self.__inserir(chave, valor, self.raiz)
        while self.raiz.anterior:
            self.raiz = self.raiz.anterior
    
    def __inserir(self, chave, valor, no):
        if no is None:
            return _2No(chave, valor)
        elif no.folha():
            if type(no) == _2No:
                return _3No(no.chave, no.valor, chave, valor)
            elif type(no) == _3No:
                no.info.append((chave, valor))
                no.info.sort(key = lambda x: x.__getitem__(0))
                pai = _2No(*no.info.pop(1))
                esq = _2No(*no.info.pop(0))
                esq.anterior = pai
                drt = _2No(*no.info.pop(0))
                drt.anterior = pai
                pai.prox = [esq, drt]
                pai = self.unir (no.anterior, pai)
                pai.anterior = no.anterior
                return pai
        else:
            if type(no) == _2No:
                if chave < no.info[0]:
                    no.prox[0] = self.__inserir(chave, valor, no.prox[0])
                elif chave > no.info[0]:
                    no.prox[1] = self.__inserir(chave, valor, no.prox[1])
                else:
                    no.info = (chave, valor)
            elif type(no) == _3No:
                if chave == no.info[0][0]:
                    no.info = [(chave, valor), (no.info[1][0], no.info[1][1])]
                elif chave == no.info[1][0]:
                    no.info = [(no.info[0][0], no.info[0][1]), (chave, valor)]
                elif chave < no.info[0][0]:
                    no.prox[0] = self.__inserir(chave, valor, no.prox[0])
                elif chave < no.info[1][0]:
                    no.prox[1] = self.__inserir(chave, valor, no.prox[1])
                else:
                    no.prox[2] = self.__inserir(chave, valor, no.prox[2])
            return no
    
    def unir(self, no1, no2):
        if no1 is None:
            return no2 
        elif type(no1) == _2No:
            if no1.info[0] < no2.info[0]:
                return _3No(no1.chave, no1.valor, no2.chave, no2.valor,
                            no1.esquerda, no2.esquerda, no2.direita)
            else:
                return _3No(no2.chave, no2.valor, no1.chave, no1.valor,
                            no2.esquerda, no2.direita, no1.direita)
        elif type(no1) == _3No:
            no1.info.append(no2.info)
            no1.prox.extend(no2.prox)
            no1.info.sort(key = lambda x:x[0])
            no1.prox.sort()
            pai = _2No(*no1.info.pop[1])
            esq = _2No(*no1.info.pop[0], no1.prox[0], no1.prox[1])
            drt = _2No(*no1.info.pop[0], no1.prox[2], no1.prox[3])
            pai.prox = [esq, drt]
            esq.anterior = drt.anterior = pai
            pai = self.unir(no1.anterior, pai)
            pai.anterior = no1.anterior
            return pai

class _2No(object):
    '''
    Classe auxiliar de nós simples. Armazena um par chave, valor e referências
    para dois nós sucessores.
    '''
    def __init__(self, chave, valor, esq = None, drt = None):
        self.info = (chave, valor)
        self.anterior = None
        self.prox = [esq, drt]
    
    def folha(self):
        '''
        Uma das características dos nós de árvores binárias balanceadas é a de
        que todas as suas folhas estão no mesmo nível. Logo, se um nó não é uma
        folha, então possui referência para todos os decendentes (direita e
        esquerda). Por tanto, basta apenas checar um dos dois para ter certeza
        se o nó é ou não uma folha.
        '''
        return self.prox[0] is None
    
    def __getattr__(self, attr):
        if attr == 'esquerda':
            return self.prox[0]
        elif attr == 'direita':
            return self.prox[1]
        elif attr == 'chave':
            return self.info[0]
        elif attr == 'valor':
            return self.info[1]
    
    def __str__(self):
        return "{}: {}".format(*self.info)
    
    def __repr__(self):
        return "({})".format(self.__str__())
    
    def __gt__(self, outro):
        return outro.__lt__(self.valor)
    
    def __lt__(self, outro):
        return outro.__gt__(self.valor)
    
    def __ge__(self, outro):
        return outro.__le__(self.valor)
    
    def __le__(self, outro):
        return outro.__ge__(self.valor)
    
    def __eq__(self, outro):
        return outro.__eq__(self.valor)

class _3No(object):
    '''
    Classe auxiliar de nós duplos. Armazena dois pares chave, valor e
    referências para três nós sucessores.
    '''
    def __init__(self, chave1, valor1, chave2, valor2, esq = None, meio = None,
                 drt = None):
        self.info = [(chave1, valor1), (chave2, valor2)]
        self.info.sort(key = lambda x: x.__getitem__(0))
        self.anterior = None
        self.prox = [esq, meio, drt]
    
    def folha(self):
        return self.prox[0] is None
    
    def __getattr__(self, attr):
        if attr == "esquerda":
            return self.prox[0]
        elif attr == "meio":
            return self.prox[1]
        elif attr == "direita":
            return self.prox[2]
        elif attr == "chave":
            return self.info[0][0], self.info[1][0]
        elif attr == "valor":
            return self.info[0][1], self.info[1][1]
    
    def __str__(self):
        return "{}: {}, {}: {}".format(self.info[0][0], self.info[0][1],
                                       *self.info[1])
    
    def __repr__(self):
        return "({})".format(self.__str__())
    
    # As comparações com os nós duplos são feitas de maneira similar as
    # comparaçãoes com os nós simples, no entanto, com exceção da igualdade, as
    # comparações são feitas com apenas um valor, seguindo a lógica descrita nos
    # métodos especiais.
    
    def __gt__(self, outro):
        return outro.__lt__(self.valor[0])
    
    def __lt__(self, outro):
        return outro.__gt__(self.valor[1])
    
    def __ge__(self, outro):
        return outro.__le__(self.valor[0])
    
    def __le__(self, outro):
        return outro.__ge__(self.valor[1])
    
    def __eq__(self, outro):
        return outro.__eq__(self.valor[0]) or outro.__eq__(self.valor[1])