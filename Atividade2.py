class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        return f"O carro {self.marca} {self.modelo} do ano {self.ano} está ligado."
    
    def desligar(self):
        return f"O carro {self.marca} {self.modelo} do ano {self.ano} está desligado."
    
c1 = Carro("Toyota", "Corolla", 2020)
print(c1.ligar())
c2 = Carro("Honda", "Civic", 2019)
print(c2.desligar())
c3 = Carro("Fusca", "Volkswagen", 1949)
print(c3.ligar())