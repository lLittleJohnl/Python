#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dist = float(input("Digite a distância em km: "))
if dist <= 200: 
 preco = dist * (0.50)
 print("O preço da viagem é de {:.2f} reais".format(preco))
elif dist > 200:
 preco = dist * (0.45)
 print("O preço da viagem é de {:.2f} reais".format(preco))