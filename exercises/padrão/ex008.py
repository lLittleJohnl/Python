#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
x = float(input("Digite o valor em metros: "))
print("O valor correspondente em centímetros é: {}".format((x*100)))
print("O valor correspondente em milímetros é: {}".format((x*1000)))