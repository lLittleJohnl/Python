#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input("Digite a velocidade: "))
print("Você foi multado no valor de {:.2f} reais".format((v-80)*0.70)) if v > 80 else print("Você está abaixo do limite de velocidade da pista")