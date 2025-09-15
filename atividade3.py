class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def verificar_aprovacao(self):
        if self.nota >= 6:
            return f"O aluno {self.nome} foi aprovado com média {self.nota:.2f}."
        else:
            return f"O aluno {self.nome} foi reprovado com média {self.nota:.2f}."
        
a1 = Aluno("Gustavo", 6)
print(a1.verificar_aprovacao())

a2 = Aluno("Adrian", 8)
print(a2.verificar_aprovacao())