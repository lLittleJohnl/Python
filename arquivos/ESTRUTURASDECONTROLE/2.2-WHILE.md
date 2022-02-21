# WHILE

## Loop while

Com o loop `while` podemos executar um conjunto de instruções enquanto uma condição for verdadeira.

### Exemplo:

```python
i = 1
while i < 6:
 print(i)
 i += 1

#Resultado:
1
2
3
4
5
```

<aside>
💡 **Nota:** lembre-se de incrementar i, ou então o loop continuará para sempre, pois o valor de i permanece inalterado, a medida que realizamos o incremente a condição é avaliada novamente.

</aside>

## A declaração break

Com a instrução `break`, podemos parar o loop mesmo se a condição while for verdadeira:

### Exemplo:

```python
i = 1
while i < 6:
 print(i)
 if i == 3:
  break  
 i += 1

#Resultado:
1
2
3
```

## A declaração continue

Com a instrução `continue`, podemos parar a iteração atual e continuar com a próxima:

### Exemplo:

```python
i = 0
while i < 6:
 i += 1  
 if i == 3:
  continue
 print(i)

#Resultado:
1
2
4
5
6
```

## A declaração else

Com a instrução `else` , podemos executar um bloco de código uma vez, quando a condição não for mais verdadeira.

### Exemplo:

```python
i = 1
while i < 6:
 print(i)  
 i += 1
else:  
 print("i não é menor que 6")

#Resultado:
1
2
3
4
5
i não é menor que 6
```