#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
x = float(input("O carro tem quantos km rodados?"))
y = int(input("Por quantos dias o carro esteve alugado?"))
print("O preço do aluguel ficará em: {:.2f}".format((y*60)+(x*0.15)))