# MATRIZES(ARRAYS)

## O que é uma matriz?

Uma matriz é uma variável especial, que pode conter mais de um valor por vez. Se você tiver uma lista de itens (uma lista de nomes de carros, por exemplo), armazenar os carros em variáveis únicas seria algo muito mais trabalhoso. A solução é montar uma matriz, pois ela pode conter muitos valores sob um único nome e você pode acessar os valores referindo-se a um índice numérico.

### Exemplo:

```python
carros = ["Model S", "Model X", "Model 3", "Model Y"]

#Não são apenas carros hehe
```

**Nota:** Python não tem suporte embutido para Matrizes, mas  podemos usar Listas para cumprir este papel, no entanto você pode importar uma biblioteca para trabalhar com matrizes, como por exemplo a biblioteca NumPy.

Essa ideia de matrizes é importante para apresentar os 4 tipos de coleções que temos em Python.

## Coleções Python (matrizes)

Existem quatro tipos de coleta de dados na linguagem de programação Python:

- **Lista** é uma coleção ordenada, mutável e que permite valores duplicados
- **Tupla** é uma coleção ordenada, imutável e que permite valores duplicados
- **Set** é uma coleção não ordenada, imutável* e não indexada, não permite valores duplicados
- **Dicionário** é uma coleção ordenada**,mutável e que não perimite valores duplicados

*  → Os *itens d*efinidos não podem ser alterados, mas você pode remover e/ou adicionar itens sempre que desejar. 

** → A partir do Python versão 3.7, os dicionários são ordenados. No Python 3.6 e anteriores, os dicionários não eram *ordenados*.

Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. Escolher o tipo certo para um determinado conjunto de dados pode significar retenção de significado e, pode significar um aumento na eficiência ou segurança.