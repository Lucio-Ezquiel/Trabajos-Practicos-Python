class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Lista para almacenar empleados (relación uno a muchos)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.empresa = self  # Relación muchos a uno, el empleado conoce su empresa

    def mostrar_empleados(self):
        print(f"Empleados de {self.nombre}:")
        for empleado in self.empleados:
            print(f"- {empleado.nombre}")

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empresa = None  # Relación muchos a uno, al principio no tiene empresa asignada

    def mostrar_empresa(self):
        if self.empresa:
            print(f"{self.nombre} trabaja en {self.empresa.nombre}.")
        else:
            print(f"{self.nombre} no tiene empresa asignada.")

# Creando una empresa
empresa1 = Empresa("TechCorp")

# Creando empleados
empleado1 = Empleado("Ana")
empleado2 = Empleado("Luis")
empleado3 = Empleado("Maria")

# Asociando los empleados a la empresa (uno a muchos)
empresa1.agregar_empleado(empleado1)
empresa1.agregar_empleado(empleado2)
empresa1.agregar_empleado(empleado3)

# Mostrando empleados de la empresa (uno a muchos)
empresa1.mostrar_empleados()

# Mostrando empresa de cada empleado (muchos a uno)
empleado1.mostrar_empresa()  # Ana trabaja en TechCorp
empleado2.mostrar_empresa()  # Luis trabaja en TechCorp
empleado3.mostrar_empresa()  # María trabaja en TechCorp