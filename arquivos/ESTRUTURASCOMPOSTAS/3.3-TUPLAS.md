# TUPLA

Tuplas são usadas para armazenar vários itens em uma única variável, seu diferencial é ser uma coleção ordenada e **imutável**.

### Exemplo

```python
tupla = ("maçã","banana","cereja") #Note que as tuplas são escritas com parênteses.
print(tupla)
```

Da perspectiva do Python, tuplas são definidas como objetos com o tipo de dados 'tupla':

```python
tupla = ("maçã","banana","cereja")
print(type(tupla))
```

## O construtor “tuple”

Também é possível usar o construtor tuple() para fazer uma tupla:

### Exemplo

```python
tupla = tuple(("maçã","banana","cereja"))
```

## $\colorbox {#228B22}{Itens de tupla}$

Os itens de tupla possuem as seguintes características:

**Ordenado:** significa que os itens têm uma ordem definida e essa ordem não mudará.

**Imutável:** significa que não podemos alterar, adicionar ou remover itens após a tupla ter sido criada.

**Indexada:** significa que o  primeiro item tem índice `[0]`, o segundo item tem índice `[1]` e assim por diante, isso nos permite utilizar rmite valores duplicados.

## $\colorbox {#228B22}{Comprimento da Tupla}$

Para determinar quantos itens uma tupla tem, use a função`len()`:

### Exemplo

```python
tupla = ("maçã","banana","cereja")
print(len(tupla))
```

## $\colorbox {#228B22}{Criar tupla com um item}$

Para criar uma tupla com apenas um item, você precisa adicionar uma vírgula após o item, caso contrário, o Python não a reconhecerá como uma tupla.

### Exemplo

```python
tupla = ("maçã",)
print(type(tupla))
#Não é uma tupla 
tupla = ("maçã")
print(type(tupla))
```

## $\colorbox {#228B22}{Itens de tupla}$

Os itens de tupla podem ser de qualquer tipo de dados.

### Exemplo

```python
tupla1 = ("maçã","banana","cereja")
tupla2 = (1, 5, 7, 9, 3)
tupla3 = (True, False, False)
#Uma tupla pode conter diferentes tipos de dados:
tupla4 = ("abc", 34, True, 40, "cara")
```

## $\colorbox {#228B22}{Acessar itens de tupla}$

Você pode acessar itens de tupla referindo-se ao número do índice, entre colchetes:

### Exemplo

```python
tupla = ("maçã","banana","cereja")
print(tupla[1]) #**Nota:** O primeiro item tem índice 0.
```

## $\colorbox {#228B22}{Indexação Negativa}$

A indexação negativa significa começar do fim.

### Exemplo

```python
tupla = ("apple", "banana", "cherry")
print(tupla[-1])
```

## $\colorbox {#228B22}{Gama de Índices}$

Você pode especificar um intervalo de índices, especificando onde começar e onde terminar o intervalo.

Ao especificar um intervalo, o valor de retorno será **uma nova tupla** com os itens especificados.

### Exemplo

```python
tupla = ("maçã","banana","cereja","laranja","kiwi","melão","manga")
print(tupla[2:5])
#Ao omitir o valor inicial, o intervalo começará no primeiro item:
tupla2 = ("maçã","banana","cereja","laranja","kiwi","melão","manga")
print(tupla2[:4])
#Ao omitir o valor final, o intervalo irá para o final da lista:
tupla3 = ("maçã","banana","cereja","laranja","kiwi","melão","manga")
print(tupla3[2:])
#Especifique índices negativos se quiser iniciar a pesquisa a partir do final da tupla:
tupla4 = ("maçã","banana","cereja","laranja","kiwi","melão","manga")
print(tupla4[-4:-1])
```

## $\colorbox {#228B22}{Verifique se o item existe}$

Para determinar se um item especificado está presente em uma tupla, use a palavra-chave`in`:

### Exemplo

```python
tupla = ("maçã","banana","cereja")
if "maçã" in tupla:  
print("Sim, 'maçã' pertence a tupla")
```

## $\colorbox {#228B22}{Alterar os valores da tupla}$

Depois que uma tupla é criada, você não pode alterar seus valores. Mas existem soluções alternativas.

1. **Converta em uma lista** : Você pode convertê-la em uma lista, adicionar os itens e convertê-la novamente em uma tupla.

### Exemplo

```python
x = ("maçã","banana","cereja")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```

Você pode utilizar esse método para remover itens ou utilizar a palavra chave `del`para deletar uma tupla.

2. **Adicione tuplas** : Você tem permissão para adicionar tuplas a tuplas.

### Exemplo

```python
tupla = ("maçã", "banana", "cereja")
tupla2 = ("laranja",)
tupla += tupla2
print(tupla)
```

### $\colorbox {#228B22}{Descompactando uma tupla}$

Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "compactação" de uma tupla,mas em Python, também podemos extrair os valores de volta para as variáveis. Isso é chamado de "desempacotamento":

### Exemplo

```python
frutas = ("maçã","banana","cereja")
(verde, amarelo, vermelho) = frutas
print(verde)
print(amarelo)
print(vermelho)
```

Se o número de variáveis for menor que o número de valores, você pode adicionar um `*` ao nome da variável e os valores serão atribuídos à variável como uma lista:

### Exemplo

```python
frutas = ("maçã","banana","cereja","morango","framboesa")
(verde, amarelo, *vermelho) = frutas
print(verde)
print(amarelo)
print(vermelho)
```

Se o asterisco for adicionado a outro nome de variável diferente do último, o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis restantes, no caso do exemplo, uma.

```python
frutas = ("maçã","manga","mamão","abacaxi","cereja")
(verde, *tropical, vermelho) = frutas
print(verde)
print(tropical)
print(vermelho)
```

## $\colorbox {#228B22}{Percorrer os números de índice}$

Você também pode percorrer os itens da tupla referindo-se ao seu número de índice. Use as funções `range()` e `len()`para criar um iterável adequado.

### Exemplo

```python
tupla = ("maçã","banana","cereja")
for i in range(len(tupla)):
 print(tupla[i])
```

## $\colorbox {#228B22}{Tuplas com Loop For}$

Você pode fazer um loop pelos itens da tupla usando um loop `for`.

### Exemplo

```python
tupla = ("maçã","banana","cereja")
for x in tupla:  
 print(x)
```

## $\colorbox {#228B22}{Tuplas com Loop While}$

Você pode percorrer os itens da lista usando um loop `while`.

Use a função `len()` para determinar o comprimento da tupla, então comece em 0 e faça um loop pelos itens da tupla referindo-se a seus índices. Lembre-se de aumentar o índice em 1 após cada iteração.

### Exemplo

```python
tupla = ("maçã","banana","cereja")
i = 0
while i < len(tupla):  
 print(tupla[i])  
i = i + 1
```

## $\colorbox {#228B22}{Junte-se a duas tuplas}$

Para juntar duas ou mais tuplas, você pode usar o operador `+`:

### Exemplo

```python
tupla1 = ("a","b","c")
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
print(tupla3)
```

## $\colorbox {#228B22}{Multiplicar tuplas}$

Se quiser multiplicar o conteúdo de uma tupla um determinado número de vezes, você pode usar o operador `*`:

### Exemplo

```python
frutas = ("maçã","banana","cereja")
tupla = frutas * 2
print(tupla)
```