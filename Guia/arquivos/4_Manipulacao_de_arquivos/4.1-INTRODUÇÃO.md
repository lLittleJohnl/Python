# INTRODUÇÃO

O manuseio de arquivos é uma parte importante de qualquer aplicativo da web.

Python tem várias funções para criar, ler, atualizar e deletar arquivos.

### Manipulação de arquivos

A função da chave para trabalhar com arquivos em Python é a função **open( ), pois ela** recebe dois parâmetros; *nome do arquivo* e *modo* .

Existem quatro métodos diferentes para abrir um arquivo:

**"r" →** Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir

**"a" →** Abrir - Abre um arquivo para anexação, cria o arquivo se não existir

**"w" →** Escrever - Abre um arquivo para escrita, cria o arquivo caso não exista

**"x" →** Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

Além disso você pode especificar se o arquivo deve ser tratado como modo binário ou texto:

**"t" →** Texto - Valor padrão. Modo de texto

**"b" →** Binário - Modo binário (por exemplo, imagens)

---

### Sintaxe

Para abrir um arquivo para leitura, basta especificar o nome do arquivo:

```python
f = open("arquivo.txt")
```

O código acima é o mesmo que:

```python
f = open("arquivo.txt", "rt")
```

Como `"r"` é para leitura e `"t"` para texto são os valores padrão, você não precisa especificá-los.

**Nota:** Certifique-se de que o arquivo existe, caso contrário você receberá um erro.