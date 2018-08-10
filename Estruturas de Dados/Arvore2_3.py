'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF 969 - Algoritmos e Estruturas de Dados

Author:     Antônio Paulino de Lima Neto (apln2)
Email:      apln2@cin.ufpe.br

                Created on Thu Aug 2 19:38:54 2018
                            
Descricao: Árvore 2-3
A construção de árvores 2-3 é relativamente complicada, então algumas mudanças
foram feitas em sua estrutura base. Para facilitar processos de ordenação e 
divisão, ao invés de atributos individuais para cada sucessor, cada chave e cada
valor, os atributos são codificados como listas de valores, facilitando assim a
separação e ordenação.


                    Licenca: The MIT License (MIT)
            Copyright(c) 2018 Antônio Paulino de Lima Neto
'''

class ArvoreBalanceada(object):
    '''
    Classe principal de árvore 2-3.
    Pode ser construída apartir de um iterável constituído de pares chave,
    valor.
    Árvores 2-3 tem como características manterem o equilibrio de seus nós, logo
    nós folha estarão sempre no mesmo nível.
    '''
    def __init__(self, iteravel = None):
        self.raiz = None
        if not iteravel is None:
            for chave, valor in iteravel:
                self.inserir(chave, valor)
    
    def inserir(self, chave, valor):
        '''
        Método de inserção.
        A maior parte do trabalho é feita na classe _No, mas, resumidamente, o
        método de inserção insere um novo par chave/valor na árvore.
        '''
        # Caso a árvore esteja vazia, um novo nó simples é criado com a chave e
        # o valor fornecidos 
        if self.raiz is None:
            self.raiz = _No(chave, valor)
        # Se já houver um nó na raiz, o método de inserção recursivo é chamado
        else:
            self.raiz._inserir(chave, valor)
    
    def buscar(self, chave):
        '''
        Busca um valor indexado pela chave fornecida na árvore. Caso não exista
        a chave fornecida, levanta uma exceção do tipo KeyError.
        '''
        return self.raiz._buscar(chave)
    
    def remover(self, chave):
        '''
        Método de remoção da árvore, busca um nó na árvore, remove e redistribui
        os valores de modo que a árvore permaneça balanceada.
        Caso a chave buscada não exista, levanta uma exceção do tipo KeyError.
        '''
        self.raiz._remover(chave)
    
    def em_ordem(self, no):
        '''
        Método de impressão em ordem.
        '''
        _str = ''
        if len(no.prox) > 0: _str += self.em_ordem(no.prox[0])+ ', ' 
        _str += "{}: {}".format(no.chave[0].__repr__(), no.valor[0].__repr__())
        if len(no.prox) > 1:
            _str += ', '
            _str += self.em_ordem(no.prox[1])
        if len(no.chave) > 1:
            _str += ', '
            _str += "{}: {}".format(no.chave[1].__repr__(),
                                    no.valor[1].__repr__())
        if len(no.prox) > 2:
            _str += ', '
            _str += self.em_ordem(no.prox[2])
        return _str

    def __getitem__(self, chave):
        '''
        Permite acessar os valor por indexação através de colchetes.
        '''
        return self.buscar(chave)
    
    def __setitem__(self, chave, valor):
        '''
        Permite adicionar valores por indexação através de colchetes.
        '''
        return self.inserir(chave, valor)
    
    def __iter__(self):
        '''
        Retorna um gerador das raízes da árvore.
        '''
        def _ponteiro(no):
            if len(no.prox) > 0: yield from _ponteiro(no.prox[0])
            yield no.chave[0]
            if len(no.prox) > 1: yield from _ponteiro(no.prox[1])
            if len(no.chave) > 1: yield no.chave[1]
            if len(no.prox) > 2: yield from _ponteiro(no.prox[2])
        return _ponteiro(self.raiz)
    
    def __repr__(self):
        return "{"+self.em_ordem(self.raiz)+"}"

class _No(object):
    '''
    Classe auxiliar Nó.
    Pode armazenar uma chave, um valor e até duas referências para subárvores
    adjacentes, ou duas chaves, dois valores e três referências para subárvores
    adjacentes.
    '''
    def __init__(self, chave, valor, antecessor = None):
        self.chave = [chave]
        self.valor = [valor]
        self.antecessor = antecessor
        self.prox = list()
    
    def folha(self):
        '''
        Retorna True se o nó for uma folha da árvore (não possuir decendentes).
        '''
        return len(self.prox) == 0
    
    def _buscar(self, chave):
        '''
        Retorna o valor indexado pela chave, caso a chave esteja na lista de
        chaves do nó. Caso contrário, chama o método de busca recursivamente no
        próximo nó decendente ou levanta uma exceção do tipo KeyError, caso o nó
        atual seja uma folha e a chave não esteja presente.
        ''' 
        if chave in self.chave:
            return self.valor[self.chave.index(chave)]
        else:
            if self.folha():
                raise KeyError(chave)
            for n in range(len(self.chave)):
                if chave < self.chave[n]:
                    return self.prox[n]._buscar(chave)
            return self.prox[-1]._buscar(chave)
    
    def _inserir(self, chave, valor):
        '''
        Caso a chave esteja no nó, atualiza o valor atual indexado pela chave
        para o valor fornecido como parâmetro. Caso não, prossegue com o método
        de inserção, unindo adicionando a chave ao nó atual, caso este seja uma
        folha ou prossegue com a busca, chamando o método de inserção
        recursivamente nos próximo nó decendente.
        '''
        cont = 0
        for key in self.chave:
            if chave == key:
                self.valor[cont] = valor
                return
            cont += 1
        if self.folha():
            self.__unir(_No(chave, valor))
        elif chave > self.chave[-1]:
            self.prox[-1]._inserir(chave, valor)
        else:
            for n in range(len(self.chave)):
                if chave < self.chave[n]:
                    self.prox[n]._inserir(chave, valor)
                    return

    def __sort(self):
        '''
        Método auxiliar pra ordenar a lista de valores de acordo com a lista de
        chaves.
        '''
        self.chave, self.valor = (list(x) for x in zip(*sorted(zip(self.chave,
                                                                self.valor)))) 
    
    def __unir(self, novo_no):
        '''
        Método auxilar que une um novo nó simples a um nó já existente na
        árvore. Quando o nó passa a ser triplo, chama o método de divisão de
        nós. 
        '''
        for no in novo_no.prox:
            no.antecessor = self
        self.prox.extend(novo_no.prox)
        self.chave.extend(novo_no.chave)
        self.valor.extend(novo_no.valor)
        self.__sort()
        self.prox.sort()
        if self.prox:
            self.prox.sort()
            for no in self.prox:
                no.antecessor = self
        if len(self.chave) > 2:
            self.__dividir()
    
    def __dividir(self):
        '''
        Esse método divide um nó triplo temporário em um nó simples com duas
        sub-árvores simples.
        Quando há um antecessor, o método unir é responsável pela união dos novo
        nó com o seu sucessor.
        ''' 
        esquerda = _No(self.chave.pop(0), self.valor.pop(0), self)
        direita = _No(self.chave.pop(1), self.valor.pop(1), self)
        if self.prox:
            self.prox[0].antecessor = self.prox[1].antecessor = esquerda
            self.prox[2].antecessor = self.prox[3].antecessor = direita
            esquerda.prox = [self.prox[0], self.prox[1]]
            direita.prox = [self.prox[1], self.prox[2]]
        self.prox = [esquerda, direita]
        
        if self.antecessor:
            if self in self.antecessor.prox:
                self.antecessor.prox.remove(self)
            self.antecessor.__unir(self)
            
                
    def __getattr__(self, attr):
        if attr == "esquerda":
            return self.prox[0]
        if attr == "meio":
            if len(self.prox) < 3:
                raise AttributeError("Nós duplos possuem apenas dois filhos")
            else:
                return self.prox[1]
        if attr == "direita":
            if len(self.prox) < 3:
                return self.prox[1]
            else:
                return self.prox[2]
    
    def __lt__(self, outro_no):
        '''
        Método especial usado para comparar dois nós usando o operador
        matemático de '<'.
        ''' 
        if not type(outro_no) == _No:
            raise TypeError
        else:
            self.chave[0] < outro_no.chave[0]
    
    def __repr__(self):
        return "({})".format(self.__texto())
    
    def __str__(self):
        return self.__texto()
    
    def __texto(self):
        '''
        Método auxiliar usado para formatar o texto antes de imprimi-lo na tela.
        '''
        _str = ''
        for chave, valor in zip(self.chave, self.valor):
            if _str: _str += ', '
            _str += "{}: {}".format(chave.__repr__(), valor.__repr__())
        return _str

numbers = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis']
a = ArvoreBalanceada()
for n in range(len(numbers)):
    a.inserir(n+1, numbers[n])