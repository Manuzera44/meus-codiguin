class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
r1 = Retangulo(5, 10)
print(f"A área do retângulo é {r1.area()} e o perímetro é {r1.perimetro()}.")
r2 = Retangulo(3, 4)
print(f"A área do retângulo é {r2.area()} e o perímetro é {r2.perimetro()}.")
#🏄‍♂️