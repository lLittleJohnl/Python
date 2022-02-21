# NÚMEROS

Existem três tipos numéricos em Python:

- `int`
- `float`
- `complex`

Variáveis de tipos numéricos são criadas quando você atribui um valor a elas:

### Exemplo:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#Para verificar o tipo de qualquer objeto em Python, use a type()função:
print(type(x))
print(type(y))
print(type(z))
```

# Int

Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado. 

```python
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
```

# Float

Float, ou "número de ponto flutuante", é um número, positivo ou negativo, que contém uma ou mais casas decimais.

```python
x = 1.10
y = 1.0
z = -35.59
w = 35e3
h = 12E4
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(h))
#Float também pode ser números científicos com um "e" para indicar a potência de 10.
```

## Complex

Os números complexos são escritos com um "j" como parte imaginária:

```python
x = 3+5j
y = 5j
z = -5j
rint(type(x))
print(type(y))
print(type(z))
```

## Conversão de Tipo

Você pode converter de um tipo para outro com o `int()`, `float()`e `complex()`métodos:

### Exemplo:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#converte de int para float:
a = float(x)
#converte de float para int:
b = int(y)
#convert de int para complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
```

<aside>
💡 **Nota:** Você não pode converter números complexos em outro tipo de número.

</aside>