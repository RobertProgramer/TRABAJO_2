class alumno:
    def __init__(self):
        self.nombre=input("Digite el nombre >> ")
        self.nota=float(input("Digite la nota de (0 a 5) >> "))

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

        if self.nota < 0 or self.nota > 5:
            print("La nota no esta dentro del rango de 0 a 5 y no se puede valorar su aprovacion del colegio")
        elif self.nota >0 and self.nota < 3:
            print(f"El estudiante {self.nombre} no aprobo con una nota de {self.nota}")
        elif self.nota <=5 and self.nota >= 3:
            print(f"El estudiante {self.nombre} aprobo con una nota de {self.nota}")


def main():
    alumno1=alumno()
    alumno1.mostrar()
  

if __name__ == "__main__":
    main()