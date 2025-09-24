class funcionário:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentosalarial(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"salário de {self.nome} é de {self.salario} depois do aumento de {percentual}%")
        else:
            print("percentual de aumento inválido")

funcionario1 = funcionário("Emanuel Cardoso", "Desenvolvedor de sistemas", 10000)
funcionario1.aumentosalarial(10)
funcionario2 = funcionário("Gustavo Fabiam", "gogo boy", 20000)
funcionario2.aumentosalarial(10)    