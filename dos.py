class cuenta:

    def __init__(self):
        self.nombre = input("Digite nombre del titular de la cuenta >>")
        self.dinero = float(input("Digite cantidad de la cuenta >>"))

    def mostrar(self):
        print (f"Titular: {self.nombre}")
        print (f"Cantidad: {self.dinero}")

class ahorro(cuenta):

    def __init__(self):
        super().__init__()
        self.plazo=input("Digite plazo a pagar >>")
        self.interes = float(input("Digite el interes a cobrar >>"))
        self.total = self.interes * self.dinero / 100

    def resultado(self):
        super().mostrar()
        print (f"Interes: {self.interes}%")
        print (f"Interes a pagar: {self.total}")
        print (f"Plazo: {self.plazo}")

class caja(ahorro):
    def __init__(self):
        super().__init__()

    def resultado2(self):
        print("___________________________________ \n")
        super().resultado()
        

def main():
    # h=ahorro()
    # h.resultado()

    h2=caja()
    h2.resultado2()

if __name__ == "__main__":
    main()