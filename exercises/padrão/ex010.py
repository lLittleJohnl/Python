#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
x = float(input("Digite o valor em reais: "))
print("É possível comprar {:.2f} dólares com este valor".format(x/5.72))