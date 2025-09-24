class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self):
        deposito = float(input(f"{self.titular} qual o valor a ser depositado?: "))
        self.saldo += deposito
        print(f"Seu saldo agora é de {self.saldo}")
    def sacar(self):
        sacar = float(input(f"{self.titular} qual o valor que será sacado?: "))
        while sacar > self.saldo:
            print("Você não tem o valor suficiente.")
            sacar = float(input(f"{self.titular} qual o valor que será sacado?: "))

            if self.saldo >= sacar:
                self.saldo -= sacar
                print(f"{self.titular} o seu saldo bancário agora é de {self.saldo}")
                
                
        
                
                

conta1 = ContaBancaria("Emanuel", 0)

conta2 = ContaBancaria("Gustavo", 0)

conta1.depositar()

conta1.sacar()
 
conta2.depositar()

conta2.sacar()

    


        
    