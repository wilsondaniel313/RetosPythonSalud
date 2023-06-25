from Salud.Persona import Persona
class Empleado(Persona):

    cargo = "Desarrollador"
    valorhora = 1000
    horastrabajadas = 100
    departamento = "Bogota"
    def calcularHonorarios(self):
        total_honorarios = (self.valorhora * self.horastrabajadas) * (1 - 0.00966)  # 0.966% de RETEICA
        return total_honorarios

    def imprimirEmpleado(self):
        print("Cargo:", self.cargo)
        print("Horas trabajadas:", self.horastrabajadas)
        print("Valor por hora:", self.valorhora)
        print("Total a pagar:", self.calcularHonorarios())

    