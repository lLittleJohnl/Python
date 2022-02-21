# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input("Digite uma frase: ").upper()
print("A letra A aparece {} vezes".format(frase.count('A')))
print("Sua primeira aparição foi no índice {}".format(frase.find('A')+1))
print("Sua última aparição foi no índice {}".format(frase.rfind('A')+1))
