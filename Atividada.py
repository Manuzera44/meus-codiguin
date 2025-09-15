class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Gustavo", 16)
print(p1.apresentar())

p2 = Pessoa("Ana", 25)
print(p2.apresentar())

p3 = Pessoa("Carlos", 30)
print(p3.apresentar())