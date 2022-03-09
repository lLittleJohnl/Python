#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = str(input("Digite o primeiro nome: "))
aluno2 = str(input("Digite o segundo nome: "))
aluno3 = str(input("Digite o terceiro nome: "))
aluno4 = str(input("Digite o quarto nome: "))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.shuffle(lista)
print("A ordem de apresentação será {}".format(lista))