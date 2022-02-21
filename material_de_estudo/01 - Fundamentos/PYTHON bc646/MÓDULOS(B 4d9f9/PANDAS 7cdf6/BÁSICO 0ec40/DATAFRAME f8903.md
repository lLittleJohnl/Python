# DATAFRAME

# O que é um DataFrame?

Um Pandas DataFrame é uma estrutura de dados bidimensional, como uma matriz bidimensional ou uma tabela com linhas e colunas.

### Exemplo:

Crie um DataFrame simples do Pandas:

```python
import pandas as pd

data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
#Carregar dados em um objeto DataFrame:
df = pd.DataFrame(data)
print(df)

#Resultado:
   calories  duration
0       420        50
1       380        40
2       390        45
```

### Localizar linha

Como você pode ver no resultado acima, o DataFrame é como uma tabela com linhas e colunas.

Pandas usam o atributo `loc` para retornar uma ou mais linhas especificadas.

### Exemplo:

Retornar linha 0:

```python
import pandas as pd

data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
df = pd.DataFrame(data)
#Se referindo a linha pelo índice:
print(df.loc[0])

#Resultado:
calories    420
duration     50
Name: 0, dtype: int64
```

**Nota:** Este exemplo retorna uma **serie**.

Retornar a linha 0 e 1:

```python
import pandas as pd

data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
df = pd.DataFrame(data)
#Veja os colchetes duplos
print(df.loc[[0,1]])

#Resultado:
   calories  duration
0       420        50
1       380        40
```

**Nota:** Ao usar `[]`, o resultado é um **DataFrame**.

### Índices nomeados

Com o argumento `index`, você pode nomear seus próprios índices.

```python
import pandas as pd

data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

#Resultado:
calories  duration
0       420        50
1       380        40
```

Você pode localizar pelos nomes que você mesmo deu aos índices.

```python
import pandas as pd

data = {
        "calories": [420, 380, 390],  
        "duration": [50, 40, 45]
       }
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"])

#Resultado:
calories    380
duration     40
Name: day2, dtype: int64
```

### Carregar arquivos em um DataFrame

Se seus conjuntos de dados estiverem armazenados em um arquivo, o Pandas poderá carregá-los em um DataFrame.

### Exemplo:

Carregue um arquivo separado por vírgula (arquivo CSV) em um DataFrame:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
```

Na próxima seção verá mais detalhes sobre o assunto.