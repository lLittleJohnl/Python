class Personagem:
     def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
p1 = Personagem("John",36)
print(p1.nome)
print(p1.idade)