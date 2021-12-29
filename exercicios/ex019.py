#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1 = str(input("Digite o primeiro nome: "))
aluno2 = str(input("Digite o segundo nome: "))
aluno3 = str(input("Digite o terceiro nome: "))
aluno4 = str(input("Digite o quarto nome: "))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))