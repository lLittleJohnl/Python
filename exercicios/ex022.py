# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem cosiderar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input("Digite um nome: ")).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
print(nome.find(' '))
