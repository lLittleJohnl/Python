#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço_produto = float(input("Digite o preço do produto: R$"))
novo_preço = preço_produto - (preço_produto * 5/100)
print("O preço do produto com o desconto é: R${:.2f}".format(novo_preço))