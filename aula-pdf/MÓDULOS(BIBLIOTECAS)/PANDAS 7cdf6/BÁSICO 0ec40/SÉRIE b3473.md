# SÉRIE

### O que é uma Série?

Uma série Pandas é como uma coluna em uma tabela, um array unidimensional que contém dados de qualquer tipo.

### Exemplo:

Crie uma série de Pandas simples a partir de uma lista:

```python
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#Resultado:
0    1
1    7
2    2
dtype: int64
```

Note que a primeira coluna do arquivo é criada pela biblioteca, é uma indexação própria, que pode ser renomeada conforme veremos ao longo do estudo.

### Rótulos(labels)

Se nada mais for especificado, os valores serão rotulados com seu número de índice. O primeiro valor tem índice 0, o segundo valor tem índice 1 e assim por diante. Este rótulo pode ser usado para acessar um valor especificado.

### Exemplo:

Retorna o primeiro valor da Série:

```python
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])

#Resultado:
1
```

### Criar rótulos

Com o argumento `index`, você pode nomear seus próprios rótulos.

### Exemplo:

Crie seus próprios rótulos:

```python
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
```

Depois de criar rótulos, você pode acessar um item consultando o rótulo.

```python
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["y"])

#Resultado:
7
```

### Objetos de chave/valor como série

Você também pode usar um objeto de chave/valor, como um dicionário, ao criar uma série.

### Exemplo:

Crie uma série de Pandas simples a partir de um dicionário:

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#Resultado:
day1    420
day2    380
day3    390
dtype: int64
```

**Nota:** As chaves do dicionário tornam-se os rótulos.

Para selecionar apenas alguns dos itens do dicionário, use o argumento `index`  e especifique apenas os itens que deseja incluir na série.

### Exemplo:

Crie uma série usando apenas dados de "day1" e "day2":

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#Resultado:
day1    420
day2    380
dtype: int64
```

### DataFrames

Os conjuntos de dados em Pandas geralmente são tabelas multidimensionais, chamadas DataFrames.

Série é como uma coluna, um DataFrame é a tabela inteira.

### Exemplo:

Crie um DataFrame de duas séries:

```python
import pandas as pd
data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
myvar = pd.DataFrame(data)
print(myvar)

#Resultado:
   calories  duration
0       420        50
1       380        40
2       390        45
```

Vamos abordar de maneira completa na seção seguinte.