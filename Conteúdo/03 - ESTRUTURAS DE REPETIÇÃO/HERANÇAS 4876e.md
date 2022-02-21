# HERANÇAS

A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.

**A classe pai** é a classe que está sendo herdada, também chamada de classe base.

**A classe filha** é a classe que herda de outra classe, também chamada de classe derivada.

## Criar uma classe pai

Qualquer classe pode ser uma classe pai, então a sintaxe é a mesma da criação de qualquer outra classe:

### Exemplo:

```python
class Pai:
    def __init__(self, pn, sn):
        self.primeiro_nome = pn
        self.sobrenome = sn
    def printnome(self):
        print(self.primeiro_nome, self.sobrenome)
x = Pai("LittleJohn,", " o brabo")
x.printnome()

#Resultado:
LittleJohn, o brabo
```

## Criar uma classe filha

Para criar uma classe que herde a funcionalidade de outra classe, envie a classe pai como parâmetro ao criar a classe filha:

### Exemplo:

```python
class Pai:
    def __init__(self, pn, sn):
        self.primeiro_nome = pn
        self.sobrenome = sn
    def printnome(self):
        print(self.primeiro_nome, self.sobrenome)
class Filho(Pai):
	pass
```

**Observação:** use a palavra chave `pass` quando não desejar adicionar outras propriedades ou métodos à classe.

Agora a classe Filho tem as mesmas propriedades e métodos que a classe Person.

### Exemplo:

```python
class Pai:
    def __init__(self, pn, sn):
        self.primeiro_nome = pn
        self.sobrenome = sn
    def printnome(self):
        print(self.primeiro_nome, self.sobrenome)
class Filho(Pai):
	pass
x = Filho("Corzon", "o rei delas")
x.printnome()

#Resultado:
Corzon, o rei delas
```

## **Adicione a função __init__()**

Até agora criamos uma classe filha que herda as propriedades e métodos de seu pai, mas podemos adicionar a função `__init__()` à classe filha se desejarmos. 

**Nota:** A função `__init__()` é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.

### Exemplo:

```python
class Pai:
    def __init__(self, pn, sn):
        self.primeiro_nome = pn
        self.sobrenome = sn
    def printnome(self):
        print(self.primeiro_nome, self.sobrenome)
class Filho(Pai):
    def __init__(self, pn, sn):
        self.comida_favorita = pn
        self.esporte_favorito = sn
    def printnome(self):
        print(self.comida_favorita, self.esporte_favorito)
x = Filho("Bolo de Murango", "e Vôlei Feminino")
x.printnome()

#Resultado:
Bolo de Murango e Vôlei Feminino
```

Note que ao adicionar a função `__init__()` a classe filha, mesmo possuindo o parâmetros com nomes iguais, ela não herdou a função `__init__()` do pai, ela substitui. Para manter a herança da função `__init__()` pai , adicione uma chamada para ela.

### Exemplo:

```python
class Pai:

    def __init__(self, pn, sn):

        self.primeiro_nome = pn
        self.sobrenome = sn

    def printnome(self):
        print(self.primeiro_nome, self.sobrenome)

class Filho(Pai):

    def __init__(self, pn, sn):
        Pai.__init__(self, pn, sn)

x = Filho("Bolo de Murango", "e Vôlei Feminino")
x.printnome()

#Resultado:
Bolo de Murango e Vôlei Feminino
#Observe que agora a frase nem faz mais sentido hahaha
```

Lembre-se que a chamada precisa ter o nome correto,Agora adicionamos com sucesso a função `__init__()` e mantivemos a herança da classe pai, estamos prontos para adicionar funcionalidades na nova função.

## Use a função super()

Python também tem uma função `super()` que fará com que a classe filha herde todos os métodos e propriedades de seu pai:

### Exemplo:

```python
class Secundario(Principal):
		def __init__(self, pn, sn):
				super().__init__(self, pn, sn)
```

Ao usar a função `super()`, você não precisa usar o nome do elemento pai, ele herdará automaticamente os métodos e propriedades de seu pai.

## Adicionar propriedades

### Exemplo:

Adicione uma propriedade chamada `formatura` à classe `Secundar`:

```python
class Student(Person):
			def __init__(self, fname, lname):
					super().__init__(fname, lname)
					self.graduationyear = 2023
```

No exemplo abaixo, o ano 2023 deve ser uma variável passada para a classe `Student`. Para isso, vamos outro parâmetro na função __init__(), que irá criar um novo objeto para a classe:

### Exemplo:

Adicione um parâmetro `year` e passe o ano correto ao criar objetos:

```python
class Student(Person):  def __init__(self, fname, lname, year):    super().__init__(fname, lname)    self.graduationyear = yearx = Student("Mike", "Olsen", 2019)
```

# Adicionar métodos

# Exemplo

Adicione um método chamado `welcome`à `Student`classe:

class Student(Person):  def __init__(self, fname, lname, year):    super().__init__(fname, lname)    self.graduationyear = year  def welcome(self):    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

[Tente você mesmo "](https://www.w3schools.com/python/trypython.asp?filename=demo_inheritance_add_method)

Se você adicionar um método na classe filha com o mesmo nome de uma função na classe pai, a herança do método pai será substituída.