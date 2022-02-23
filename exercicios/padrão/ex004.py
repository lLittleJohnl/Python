# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
# Detalhe da função input é o padrão de entrada é sempre str.
dados = input("Digite algo: ") #Entrada
print("O tipo primitivo desse valor é:", type(dados)) #Qual é o tipo de dados?
print("O valor é composto por letras?", dados.isalpha())
print("O valor é composto por números?", dados.isalnum())