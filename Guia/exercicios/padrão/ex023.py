# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input("Informe um número: ")
print("Unidade: {}".format(num[3]))
print("Dezena: {}".format(num[2]))
print("Centena: {}".format(num[1]))
print("Milhar: {}".format(num[0]))
