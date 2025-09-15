class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def calcular_total(self):
        return self.preco * self.quantidade
        
p1 = Produto("Teclado mecânico", 150, 10)
print(f"O preço total do produto {p1.nome} é R$ {p1.calcular_total():.2f}.")

p2 = Produto("Monitor", 1200, 5)
print(f"O preço total do produto {p2.nome} é R$ {p2.calcular_total():.2f}.")

p3 = Produto("Mouse", 80, 20)
print(f"O preço total do produto {p3.nome} é R$ {p3.calcular_total():.2f}.")
#🏄‍♂️