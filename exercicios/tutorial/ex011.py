#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
Area = largura * altura
print("Será necessário {} de tinta em litros para realizar a pintura da parede".format(Area/2))