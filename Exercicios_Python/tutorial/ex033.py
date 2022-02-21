#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("Primeiro número:"))
n2 = float(input("Segundo número:"))
n3 = float(input("Terceiro número:"))
menor = n1
if n2 < n1 and n2 < n3: 
 menor = n2
if n3 < n1 and n3 < n2: 
 menor = n3
maior = n1
if n2 > n1 and n2 > n3: 
 maior = n2
if n3 > n1 and n3 > n2:
 maior = n3
print("O menor é {} e o maior é {}".format(menor, maior))