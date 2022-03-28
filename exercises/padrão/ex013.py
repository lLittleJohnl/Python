#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input("Digite o salário atual: R$"))
ns = s + (s * 15/100)
print("O salário com reajuste será de : R${:.2f}".format(ns))