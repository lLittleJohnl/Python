# CRIAR E GRAVAR ARQUIVO

### Criar um novo arquivo

Para criar um novo arquivo em Python, use o método `open()`, com um dos seguintes parâmetros:

`"x"`- Criar - criará um arquivo, retornará um erro se o arquivo existir

`"a"`- Append - criará um arquivo se o arquivo especificado não existir

`"w"`- Write - criará um arquivo se o arquivo especificado não existir

### Exemplo:

Crie um arquivo chamado "novoarquivo.txt":

```python
f = open("novoarquivo.txt", "x")
```

Resultado: um novo arquivo vazio é criado!

# Gravar em um arquivo existente

Para gravar em um arquivo existente, você deve adicionar um parâmetro à função `open()`:

`"a"`- Append - anexará ao final do arquivo

`"w"`- Write - substituirá qualquer conteúdo existente

### Exemplo:

Abra o arquivo "novoarquivo.txt" e anexe o conteúdo ao arquivo:

```python
f = open("novoarquivo.txt", "a")
f.write("Agora o arquivo não está mais vazio!")

f.close()

#abra e leia o arquivo após o anexo:
f = open("novoarquivo.txt", "r")
print(f.read())
```

### Exemplo:

Abra o arquivo "novoarquivo.txt" e sobrescreva o conteúdo:

```python
f = open("novoarquivo.txt", "w")
f.write("Eu deletei o conteúdo todo sem querer querendo!")

f.close()

#abra e leia o arquivo após o anexo:
f = open("novoarquivo.txt", "r")
print(f.read())
```

**Nota:** o método "w" substituirá o arquivo inteiro.