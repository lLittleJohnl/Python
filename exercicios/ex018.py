#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import (sin, cos, tanh, radians)
import math
ang = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(ang))
print("O seno do ângulo vale {:.2f} rad.".format(sen))
cos = math.cos(math.radians(ang))
print("O cosseno do ângulo vale {:.2f} rad.".format(cos))
tan = math.tanh(math.radians(ang))
print("A tangente do ângulo vale {:.2f} rad.".format(tan))