# MÓDULOS

## O que é um módulo?

Considere um módulo igual a uma biblioteca de código. Um arquivo que contém um conjunto de funções que você deseja incluir em seu aplicativo. Você mesmo pode criar um módulo. Existem infinitos módulos no site oficial de Python.

## Importar do Módulo

Você pode importar um módulo utilizando a instrução `import`:

### Exemplo:

```python
import math
x = 4
raiz_x = math.sqtr(x) #função raiz quadrada
print(raiz_x)

#Resultado:
2.0
```

Quando desejamos utilizar apenas uma funcionalidade podemos usar a palavra-chave `from`:

### Exemplo:

```python
from math import sqrt
x = float(input("Digite um número: ")) #Você pode escolher o número
raiz_x = sqrt(x)
print(raiz_x) 
```

**Nota:** Ao importar usando a palavra - chave `from` , você importa o método diretamente para sua pasta e não há necessidade de utilizar o nome do módulo ao referir-se aos seus elementos.

---

## Criando um Módulo

Para criar um módulo basta salvar o código desejado em um arquivo com a extensão de arquivo `.py`:

### Exemplo:

```python
def modulo(nome):
 print("Olá, " + nome)
```

Para utilizar, basta importá-lo como aprendemos anteriormente.

## Características de um Módulo

O módulo pode conter funções, conforme já descrito, mas também variáveis de todos os tipos (arrays, dicionários, objetos etc):

Você pode nomear o arquivo do módulo como quiser, mas deve ter a extensão do arquivo `.py`.Você pode criar um alias(um alias é um segundo nome para um dado) ao importar um módulo, usando a palavra-chave `as`.

### Exemplo:

Crie um alias para `mymodule`chamado `mx`:

```python
import mymodule as mx 
a = mx.person1["age"]
print(a)
```

# Função dir ()

A função `dir()` é uma função incorporada para listar todos os nomes de função (ou nomes de variáveis) em um módulo.

### Exemplo:

```python
import math
x = dir(math)
print(x)

#Resultado: 
['**doc**', '**loader**', '**name**', '**package**', '**spec**', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

**Nota:** A função dir () pode ser usada em *todos os* módulos, inclusive aqueles que você mesmo cria.