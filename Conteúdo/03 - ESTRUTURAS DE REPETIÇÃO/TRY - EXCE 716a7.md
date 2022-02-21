# TRY - EXCEPT

O bloco `try` permite testar um bloco de código para erros.

O bloco`except` permite lidar com o erro.

O bloco`finally` permite que você execute código, independentemente do resultado dos blocos try e except.

# Manipulação de exceção

Quando ocorre um erro, ou exceção, como o chamamos, o Python normalmente para e gera uma mensagem de erro.

Essas exceções podem ser tratadas usando a instrução`try`:

### Exemplo

O bloco `try` irá gerar uma exceção, pois `x`não está definido:

> `try:  
print(x)
except:
print("An exception occurred")`
> 

Uma vez que o bloco try gera um erro, o bloco except será executado.

Sem o bloco try, o programa irá travar e gerar um erro:

### Exemplo

Esta declaração irá gerar um erro, porque `x`não está definida:

> `print(x)`
> 

### Muitas exceções

Você pode definir quantos blocos de exceção quiser, por exemplo, se quiser executar um bloco especial de código para um tipo especial de erro:

### Exemplo

Imprima uma mensagem se o bloco try gerar um `NameError`e outra para outros erros:

> `try:  
print(x)
except NameError:  
print("Variable x is not defined")
except:  
print("Something else went wrong")`
> 

### Else

Você pode usar a palavra-chave `else` para definir um bloco de código a ser executado se nenhum erro for gerado:

Neste exemplo, o bloco `try` não gera nenhum erro:

> `try:
print("Hello")
except:
print("Something went wrong")
else:
print("Nothing went wrong")`
> 

### Finally

O `finally`bloco, se especificado, será executado independentemente se o bloco try levanta um erro ou não.

> `try:
print(x)
except:
print("Something went wrong")
finally:
print("The 'try except' is finished")`
> 

This can be useful to close objects and clean up resources:

# Example

Try to open and write to a file that is not writable:

try:  f = open("demofile.txt")  try:    f.write("Lorum Ipsum")  except:    print("Something went wrong when writing to the file")  finally:    f.close()except:  print("Something went wrong when opening the file")

The program can continue, without leaving the file object open.

# Raise an exception

As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the `raise` keyword.

# Example

Raise an error and stop the program if x is lower than 0:

x = -1if x < 0:  raise Exception("Sorry, no numbers below zero")

The `raise` keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

# Example

Raise a TypeError if x is not an integer:

x = "hello"if not type(x) is int:  raise TypeError("Only integers are allowed")