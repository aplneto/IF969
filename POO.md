# Programção Orientada a Objetos


#####Aviso!
Esse é um guia rápido sobre o paradigma de orientação a objetos, então pode (e provavelmente vai) faltar informação ou detalhamento em determinados aspectos. No entanto, para aqueles com dúvidas sobre o uso de orientação a objetos em Python ou sobre a orientação a objetos em si, esse guia pode ser de alguma ajuda.
Para um melhor aprendizado sobre programação orientada a objetos, cheque as referências.
#####Programação Estruturada
O paradigma de programação estruturado enfatisa o uso de subrotinas, laços de repetição, condicionais e estruturas em bloco na solução de problemas.
Basicamente, as subrotinas são escritas e aplicadas a um determinado tipo de informação. Por exemplo:

```python
def acharletra(string, letra):
	cont = 0
	for char in string:
		if char == letra:
			return cont
		else:
			cont += 1
	return -1
```
Dados uma string e um caractere, o código acima encontra a primeira ocorrência do caractere na string e retorna o índice dessa ocorrência. Por exemplo:

```python
st = "Isac é lindo"
print(acharletra(st, 'é'))
>>> 5
```

Apesar de ser uma função útil, podemos observar que ela não term utilidade para, por exemplo, um objeto não iterável, como um inteiro, um float, um booleano...
Se imaginarmos os tipos de dados como objetos palpáveis da vida real, temos que o controle das funcionalidades desses objetos estão sempre separados deles. É como ter, por exemplo, um *microondas* e, separadamente, um botão ou interrupetor que o liga, mas que não faz parte do *microondas*.
A programação orientada a objetos tenta aproximar a programação da vida real nesse aspecto.
#####Programação Orientada a Objetos
Na programação orientada a objetos, as funções que os objetos podem cumprir estão acopladas a eles, são chamadas de métodos.
No exemplo anterior, por exemplo, uma variável do tipo *microondas* teria um método responsável pelo seu ligamento, outro método responsável pelo desligamento, outro responsável pelo controle do contador, da potência... e assim sucessivamente. Na programação orientada a objetos, as funcionalidades dos tipos de objetos são seus métodos.
Assim como funcionalidades, objetos da vida real também possuem características, podendo essas serem, ou não, mutáveis. Um objeto do tipo microondas, por exemplo, poderia ter as caracteríticas volume, peso, capacidade... em programação orientada a objetos, essas características também estão acopladas ao objeto e são chamadas de atributos.

#####Características da POO
As características principais da programação orientada a objetos são a **Abstração**, **Herança**, **Polimorfismo** e **Encapsulamento**.

**Abstração**:É utilizada para a definição de entidades do mundo real. Sendo onde são criadas as classes. Essas entidades são consideradas tudo que é real, tendo como consideração as suas características e ações.
Em Python, a palavra _class_ é reservada a criação de Classes (objetos).

| Entidade | Características | Ações |
|:--------|:---------------|:-----|
| carro   | tamanho, cor, peso, altura | acelerar, parar, ligar, dirigir |
| elevador | tamanho, peso máximo | subir, descer, escolher andar |
| conta bancária | saldo, limite, número | depositar, sacar, ver extrato |


```python
class Conta:
	def __init__(self, saldo, limite, num):
		self.saldo = saldo
		self.lim = limite
		self.num = num
	
	def depositar(self, valor):
		if self.saldo + valor < self.lim:
			self.saldo += valor
		else:
			print("Sua conta não tem limite suficiente")
	
	def sacar(self, valor):
		if self.saldo >= valor:
			self.saldo -= valor
		else:
			print("Você não tem saldo suficiente")
	
	def ver_extrato(self):
		print(self.saldo)
```

Por exemplo, acima, a abstração do objeto Conta Bancária.

**Herança**: O significado de herança é similar ao significado usado no mundo real, onde filhos herdam certas características dos pais. Em programação orientada a objetos, um objeto pode herdar atributos e métodos de um outro objeto, sendo a classe herdeira chamada subclasse e a classe pai chamada superclasse.
Uma das grandes vantagens da herança é a reutilização de código, ideal para quando há classes que compartilham de um mesmo atributo ou método.

![Hierarquia de Classes](https://img-21.ccm2.net/TFkixX1LWid1t6x1h3AancR9t-I=/56fc4b0ee402409cad1d4294085ab1f7/ccm-encyclopedia/poo-images-animaux2.gif)
######No esquema de classe acima, Animal é a superclasse da qual Herbívoro e Carnívoro herdam características. A classe herbivoro herda características de ambas, Herbívoro e Carnívoro.

Em Python 3, todos os objetos herdam características da classe built-in object.

**Polimorfismo**: Polimorfismo está relacionado com herança, de modo que representa a possibilidade de sobrescritura de métodos e atributos.
Duas classes distintas podem ter métodos que compartilham o mesmo nome, mas que funcionam de maneira diferente, ou possuem parâmetros diferentes.

**Encapsulamento**: É a ideia de esconder do usuário determinadas ideias ou detalhes internos, tornando partes do sistema o mais independente possível. Imagine, por exemplo, um controle remoto de televisão. Quando um usuário assistindo TV pressiona o botão de mudança de canal, não importa para o usuário o processo que faz com que a televisão troque de canal, apenas que ela execute a sua função com sucesso. Esse é um exemplo de encapsulamento.

#Objetos em Python - Guia Relâmpago

Para declarar um novo objeto em Python, usa-se a palavra reservada _Class_ seguida pelo nome da classe.
Caso a classe que você está declarando herde características de uma ou mais classes já existentes, após declarar o nome da classe, entre parêntesis, você deve declarar as classes da qual ela herda características.

```python
class Coisa():
```
Ou ainda:

```python
class OutraCoisa(Coisa):
```

A primeira classe é uma superclasse, não herda características de nenhuma outra classe. Já a classe OutraCoisa herda características da classe Coisa, sendo então uma subclasse desta.

O momento de instanciação de uma variável é o momento em que a variável passa a existir. Se essa variável for um objeto, essa instanciação acontece através de um método especial (dunder methods, magic methods). Métodos especiais são métodos com características especificas de Python, eles são marcados por dois underlines antes e depois do nome.
O método especial que controla o momento de instanciação de uma variável é o init.

```python
class Funcionario():
	def __init__ (self, nome, idade, cpf, matricula):
		self.nome = nome
		self.idade = idade
		self.cpf = cpf
		self.matricula = matricula
```