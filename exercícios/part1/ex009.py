#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
x = int(input("Digite o número: "))
i = 0
while i < 11:
 print("{} x {:2} = {}".format(x,i,(x*i)))
 i += 1
