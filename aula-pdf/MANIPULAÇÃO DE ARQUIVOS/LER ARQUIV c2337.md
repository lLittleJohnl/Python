# LER ARQUIVO

# Abra um arquivo no servidor

Suponha que temos o seguinte arquivo, localizado na mesma pasta do Python:

**nome:** arquivo.txt

**Conteúdo:** Olá! Bem-vindo ao arquivo.txt
          Este arquivo é para fins de teste.

Para abrir o arquivo, use a função interna **open( ),** ela retorna um objeto de arquivo, que possui um método **read( )** para leitura do conteúdo do arquivo:

### Exemplo:

```python
f = open("arquivo.txt", "r")
print(f.read())
```

Se o arquivo estiver localizado em um local diferente, você terá que especificar o caminho do arquivo, assim:

### Exemplo:

```python
f = open("D:\\myfiles\\welcome.txt", "r")
print(f.read())
```

# Detalhes importantes

É uma boa prática sempre fechar o arquivo quando terminar, pois em alguns casos, devido ao buffer, as alterações feitas em um arquivo podem não aparecer até que você feche o arquivo. Para realizar essa tarefa utilizamos o método **close( ):**

### Exemplo:

```python
f = open("arquivo.txt", "r")
print(f.readline())

f.close()
```

## Características dos métodos

Por padrão, o método **read( )** retorna o texto inteiro, mas você também pode especificar quantos caracteres deseja retornar:

### Exemplo:

```python
#Retorna os 5 primeiros caracteres do arquivo
f = open("arquivo.txt", "r")
print(f.read(**5**))

f.close()

#Resultado:
Bem-vindo
```

Você pode retornar uma linha usando o método **readline( )**:

### Exemplo:

Leia uma linha do arquivo:

```python
f = open("arquivo.txt", "r")
print(f.readline())

f.close()
```

Ao usar o método **readline( )** duas vezes, você pode ler as duas primeiras linhas:

```python
f = open("arquivo.txt", "r")
print(f.readline())
print(f.readline())

f.close()
```

Fazendo um loop pelas linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:

```python
f = open("arquivo.txt", "r")
for x in f:  
	print(x)
```