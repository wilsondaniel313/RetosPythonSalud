
class Persona:
    def __init__(self):
        self.tipoDoc = ""
        self.documento = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirDatos(self):
        self.tipoDoc = input("Ingrese el tipo de documento: ")
        self.documento = input("Ingrese el número de documento: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.peso = float(input("Ingrese el peso en kg: "))
        self.estatura = float(input("Ingrese la estatura en metros: "))
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo: ")

    def mostrarPersona(self):
        print("Tipo de documento:", self.tipoDoc)
        print("Documento:", self.documento)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Peso:", self.peso, "kg")
        print("Estatura:", self.estatura, "m")
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)

    def calcularImc(self):
        indiceMasaCorporal = self.peso / self.estatura*2
        if indiceMasaCorporal <=20:
            print("El peso está por debajo del ideal",self.peso,"Kg")
        elif indiceMasaCorporal >= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")
        return indiceMasaCorporal
      
        


    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("Es menor de Edad")
            
