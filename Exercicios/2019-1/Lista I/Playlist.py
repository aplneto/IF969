# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:13:59 2019

@author: apln2
"""

class _No:
    '''
    Classe auxiliar
    Usada dentro da programação das classes das estruturas lineares.
    A lista implementada abaixo é uma lista de encadeamento simples, ou seja,
    os nós possuem apenas uma referência, para o nó seguinte.
    '''
    def __init__(self, valor, seguinte = None):
        self.valor = valor
        self.seguinte = seguinte
    
    def __str__(self):
        '''
        Esse é o método usado para imprimir um objeto usando a função print.
        
        :return str: esse método deve, obrigatoriamente, retornar uma string
        '''
        return str(self.valor)

class Lista:
    '''
    Classe principal
    A classe lista é um conjunto de nós alinhados a partir de um nó estrutural,
    muitas vezes chamados de nó cabeça ou nó sentinela.
    '''
    def __init__(self):
        '''
        A lista começa vazia, então, nesse caso o único nó presente na lista é
        o sentinela.
        O nó sentinela é um nó intermediário que fica entre o início e o fim da
        lista.
        '''
        self.sentinela = _No(None)
    
    def anexar(self, valor):
        '''
        Anexar um valor a uma lista é equivalente a uma inserção no fim da
        lista.
        Anexação ocorre encontrado o último elemento da lista e, inserindo após
        ele um novo nó.
        '''
        pos = self.sentinela
        while pos.seguinte is not None:
            pos = pos.seguinte
        pos.seguinte = _No(valor)
    
    def __str__(self):
        '''
        Método de exibição.
        '''
        _str = ''
        pos = self.sentinela.seguinte
        while pos is not None:
            if _str: _str += ', '
            _str += pos.valor.__str__()
            pos = pos.seguinte
        return '[{}]'.format(_str)

class Musica:
    def __init__(self, titulo, dur):
        self.titulo = titulo
        self.tempo = dur
    
    def __str__(self):
        return "{} - {}".format(self.titulo, self.tempo)

class Playlist(Lista):
    '''
    A implementação de uma subclasse Playlist foi feita para auxiliar a leitura
    de comandos na função.
    '''
    def __init__(self):
        '''
        Usaremos um ponteiro para marcar a posição na qual a lista se encontra.
        A partir do ponteiro iremos executar os comandos a medida que eles são
        executados.
        Veja mais detalhes na documentação de cada comando.
        '''
        Lista.__init__(self)
        self.ponteiro = self.sentinela
    
    def reproduzir(self):
        '''
        Considerando que o ponteiro começa no sentinela (um nó estrutural, que
        não possui valor guardado), a reprodução começa a partir do nó
        seguinte.
        Então para reproduzir é necessário avançar a posição do ponteiro para o
        próximo nó e então executar.
        '''
        self.ponteiro = self.ponteiro.seguinte
        
        # A execução é representada pelo retorno do valor do nó, no caso dessa
        # implementação, um objeto do tipo música.
        
        return self.ponteiro.valor
    
    def repetir(self):
        '''
        Uma vez que o método de reprodução avança o ponteiro para a próxima
        música, o método de repetição não avança o ponteiro, apenas retorna o
        valor que já foi reproduzido uma vez.
        '''
        return self.ponteiro.valor
    
    def pular(self):
        '''
        O método de avanço de música ignora a próxima música que seria
        executada. Nesse caso, o ponteiro avança, mas não há reprodução.
        '''
        self.ponteiro = self.ponteiro.seguinte
    
    def finalizar(self):
        '''
        O método de finalização da playlist coloca o ponteiro depois da útlima
        música.
        Dependeno da implementação, o novo valor do ponteiro passa a ser o
        sentinela (valor inicial) ou None.
        '''
        self.ponteiro = None

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        p = Playlist()
        M = int(input())
        for m in range (M):
            titulo = input()
            dur = float(input())
            p.anexar(Musica(titulo, dur))
        comandos = input()
        tempo = 0
        reproduzidas = ''
        for c in comandos:
            if c == 'r':
                musica = p.reproduzir()
                tempo += musica.tempo
                if reproduzidas: reproduzidas += ', '
                reproduzidas += musica.titulo
            elif c == 'v':
                musica = p.repetir()
                tempo += musica.tempo
                if reproduzidas: reproduzidas += ', '
                reproduzidas += musica.titulo
            elif c == 'p':
                musica = p.pular()
            else:
                p.finalizar()
                break
        print("Viagem {}: {}".format(t+1, tempo))
        print(reproduzidas)