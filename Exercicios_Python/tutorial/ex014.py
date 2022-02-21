#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
x = float(input("Digite um valor de temperatura em Celsius(°C): "))
K = x + 273
F = 1.8*x + 32
print("O valor correspondente em Farenheit(°F):{}".format(F))
print("O valor correspondente em Kelvin(K):{}".format(K))