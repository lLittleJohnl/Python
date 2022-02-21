# INTRODUÇÃO

Pandas é uma biblioteca Python.

Pandas é usado para analisar dados.

### O que é Panda?

Pandas é uma biblioteca Python usada para trabalhar com conjuntos de dados.

Possui funções para analisar, limpar, explorar e manipular dados.

O nome "Pandas" tem uma referência a "Panel Data" e "Python Data Analysis" e foi criado por Wes McKinney em 2008.

### Por que usar pandas?

O Pandas nos permite analisar big data e tirar conclusões com base em teorias estatísticas.

Os pandas podem limpar conjuntos de dados confusos e torná-los legíveis e relevantes.

Dados relevantes são muito importantes na ciência de dados.

> **Data Science:** é um ramo da ciência da computação onde estudamos como armazenar, usar e analisar dados para derivar informações deles.
> 

---

### O que os pandas podem fazer?

O Pandas fornece respostas sobre os dados. Como:

- Existe uma correlação entre duas ou mais colunas?
- O que é valor médio?
- Valor máximo?
- Valor mínimo?

Os pandas também podem excluir linhas que não são relevantes ou contêm valores errados, como valores vazios ou NULL. Isso é chamado *de limpeza* dos dados.

### Onde está a base de código do Pandas?

O código-fonte do Pandas está localizado neste repositório do github: [https://github.com/pandas-dev/pandas](https://github.com/pandas-dev/pandas)

> **github:** permite que muitas pessoas trabalhem na mesma base de código.
> 

### Instalação de pandas

Se você já tem o [Python](https://www.w3schools.com/python/default.asp) e o [PIP](https://www.w3schools.com/python/pandas/python_pip.asp) instalados em um sistema, a instalação do Pandas é muito fácil.

Instale-o usando este comando:

C:\Users\*Your Name*>pip install pandas

Se este comando falhar, use uma distribuição python que já tenha o Pandas instalado, como Anaconda, Spyder etc.

---

### Importar pandas

Depois que o Pandas estiver instalado, importe-o em seus aplicativos adicionando a palavra-chave `import`:

```python
import pandas
```

Agora o Pandas está importado e pronto para uso.

Vamos ver um exemplo para iniciar nossos estudos.

### Exemplo:

```python
import pandas

mydataset = {
            'cars': ["BMW", "Volvo", "Ford"],  
            'passings': [3, 7, 2]
            }
myvar = pandas.DataFrame(mydataset)
print(myvar)

#Resultado
```