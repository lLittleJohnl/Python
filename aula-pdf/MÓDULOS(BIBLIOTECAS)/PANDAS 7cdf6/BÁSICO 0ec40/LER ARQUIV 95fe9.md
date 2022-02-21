# LER ARQUIVO JSON

Os conjuntos de big data geralmente são armazenados ou extraídos como JSON, que é basicamente um arquivo de  texto simples, mas tem o formato de um objeto, e é bem conhecido no mundo da programação.

Em nossos exemplos, usaremos um arquivo JSON chamado 'data.json':[Abra data.json](https://www.w3schools.com/python/pandas/data.js) .

### Exemplo:

Carregue o arquivo JSON em um DataFrame:

```python
import pandas as pd

df = pd.read_json('data.json')
print(df.to_string())
```

---

# Dicionário como JSON

**JSON = Dicionário Python**

Os objetos JSON têm o mesmo formato dos dicionários Python.

Se seu código JSON não estiver em um arquivo, mas em um Dicionário Python, você poderá carregá-lo diretamente em um DataFrame:

# Exemplo

Carregue um dicionário Python em um DataFrame:

import pandas as pddata = {  "Duration":{    "0":60,    "1":60,    "2":60,    "3":45,    "4":45,    "5":60  },  "Pulse":{    "0":110,    "1":117,    "2":103,    "3":109,    "4":117,    "5":102  },  "Maxpulse":{    "0":130,    "1":145,    "2":135,    "3":175,    "4":148,    "5":127  },  "Calories":{    "0":409,    "1":479,    "2":340,    "3":282,    "4":406,    "5":300  }}df = pd.DataFrame(data)print(df)