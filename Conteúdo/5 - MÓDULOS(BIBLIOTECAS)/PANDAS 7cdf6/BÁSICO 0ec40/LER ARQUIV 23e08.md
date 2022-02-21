# LER ARQUIVO CSV

Uma maneira simples de armazenar grandes conjuntos de dados é usar arquivos CSV (arquivos separados por vírgula).

Os arquivos CSV contêm texto simples e é um formato bem conhecido que pode ser lido por todos, incluindo Pandas.

Em nossos exemplos, usaremos um arquivo CSV chamado 'data.csv'.

### Exemplo:

Carregue o CSV em um DataFrame:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
```

Se você tiver um DataFrame grande com muitas linhas, o Pandas retornará apenas as 5 primeiras linhas e as últimas 5 linhas como você bem percebeu

**Dica:** Use `to_string()` para imprimir todo o DataFrame.

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())
```

### Retorno de linhas

O número de linhas retornadas é definido nas configurações de opção do Pandas.

Você pode verificar o número máximo de linhas do seu sistema com a instrução `pd.options.display.max_rows`.

### Exemplo:

Verifique o número máximo de linhas retornadas:

```python
import pandas as pd
print(pd.options.display.max_rows)
```

No meu sistema o número é 60, o que significa que se o DataFrame contiver mais de 60 linhas, a instrução `print(df)` retornará apenas os cabeçalhos e as primeiras e últimas 5 linhas.

Você pode alterar o número máximo de linhas com a mesma instrução.

### Exemplo:

Aumente o número máximo de linhas para exibir todo o DataFrame:

```python
import pandas as pd

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
```

Nessa seção não foi possível colocar os exemplos por questão de não ser prático ficar reproduzindo o arquivo repetidamente, mas assim como nas outras ocasiões, rode o código você mesmo e tire suas próprias conclusões.