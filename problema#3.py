var = 0
class cliente():
    def __init__(self):
        self.nombre = input("Digita nombre >>")
        self.identificacion = int(input("Digita identificacion >>"))

    def depositar(self):
        self.deposito= float(input("Dinero a depositar >>"))

    def extraer(self):
        if self.deposito <= 0:
            print("No tiene dinero en la cuenta o debe")
            self.salida=0
        else:
            self.salida = float(input("Cuanto desea sacar >>"))
            
                            
    def mostrar(self):
        print(f"Nombre >> {self.nombre}")
        print(f"Identificacion >> {self.identificacion}")
        print(f"Deposito >> {self.deposito}")
        
        if self.salida > self.deposito or self.salida < 0:
            print(f"Saldo insuficiente para retirar {self.salida}")
        else:
            print(f"Retiro >> {self.salida}")

class banco(cliente):
    def __init__(self):
        super().__init__()

    def operar(self):
        super().depositar()
        super().extraer()
        self.depFinal = self.deposito - self.salida

    def depositoFinal(self):
        print("___________________________________ \n")
        super().mostrar()
        if self.depFinal < 0:
            print(f"Deberia al banco o obtenga un avance superior al monto a retirar")
        else:
            print(f"Saldo total {self.depFinal}")


def main():
    b=banco()
    b.operar()
    b.depositoFinal()

if __name__ == "__main__":
    main()