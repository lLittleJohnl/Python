#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# 3 segmentos de reta a, b e c respectivamente. Um triângulo pode ser formado se e somente se a < b + c.
r1 = int(input("Digite o comprimento do primeiro segmento de reta: "))
r2 = int(input("Digite o comprimento do segundo segmento de reta: "))
r3 = int(input("Digite o comprimento do terceiro segmento de reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
 print("É possível formar um triângulo com os segmentos de reta")
else: 
 print("Não é possível formar um triângulos com os segmentos de reta")