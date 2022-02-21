# LAMBDA

Uma função lambda é uma pequena função anônima que pode receber qualquer número de argumentos, mas só pode ter uma expressão.

## Sintaxe

lambda *argumentos* : *expressão*

A expressão é executada e o resultado é retornado:

### Exemplo:

```python
x = lambda a : a + 10
print(x(5))

#Resultado:
15
#Toma o valor de a, acrescenta 10 e imprime
```

As funções lambda podem receber qualquer número de argumentos.

### Exemplo:

```python
x = lambda a, b : a * b
print(x(5, 6))

#Resultado:
30
#Toma o valor de a e b, realiza o produto e imprime
```

## Por que usar funções Lambda?

O poder do lambda é mostrado quando você usa como uma função anônima dentro de outra função. Digamos que você tenha uma definição de função que leva um argumento, e esse argumento será multiplicado por um número desconhecido:

```python
def funcao(n):  
 return lambda a : a * n
```

Use essa definição de função para fazer uma função que sempre duplica o número que você envia.

### Exemplo:

```python
def funcao(n):
 return lambda a : a * n
dobro = funcao(2)
print(dobro(11))

#Resultado:
22
```

Use funções lambda quando uma função anônima for necessária por um curto período de tempo.