class Aluno():
    def __init__(self, nome, curso, notas):
        self.nome = nome
        self.curso = curso
        self.notas = []
        
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        
    def media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0
    
    def mostrar_info(self):
        return f"Nome: {self.nome}, Curso: {self.curso}, Notas: {self.notas}, Média: {self.media():.2f}"
    
a1 = Aluno("Gustavo", "Desenvolvimento de Sistemas", [])
a1.adicionar_nota(8)
a1.adicionar_nota(7.5)
a1.adicionar_nota(9)
print(a1.mostrar_info())

a2 = Aluno("Adrian Holz", "Desenvolvimento de Sistemas", [])
a2.adicionar_nota(9)
a2.adicionar_nota(8.5)
a2.adicionar_nota(10)
print(a2.mostrar_info())