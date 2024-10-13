class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario < 0:
            print("El salario no puede ser negativo")
        else:
            self._salario = nuevo_salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        return f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: {self.salario}"

# Uso de las clases
empleado1 = Empleado("Carlos", 2500)
empleado1.salario = 2700  # Cambiando el salario
print(empleado1.mostrar_informacion())

gerente1 = Gerente("Ana", 5000, "Ventas")
print(gerente1.mostrar_informacion())