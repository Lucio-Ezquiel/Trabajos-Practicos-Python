"""
Sistema de Gestión de Inventario de Tienda
Descripción:
Una tienda de tecnología necesita llevar un registro de su inventario. Cada producto
tiene asociado un código, una descripción, y un precio. Además, el sistema debe ser
capaz de:
Mostrar todos los productos disponibles.
Buscar un producto por su código.
Modificar el precio de un producto.
Eliminar un producto del inventario.
Mostrar todos los productos cuyo precio esté en un rango dado por el usuario.
Para realizar este ejercicio, usa las siguientes estructuras:
Tuplas para almacenar los detalles de cada producto (código, descripción,
precio).
Diccionarios para almacenar el inventario, donde el código del producto será la
clave y el valor será una tupla con la descripción y el precio.
Instrucciones:
1. Crear un diccionario que contenga el inventario inicial con al menos 5
productos.
* Cada clave será un código de producto (ej. "A001", "A002").
* Cada valor será una tupla con la descripción del producto y su precio.
2. Implementar las siguientes funciones:
* mostrar_inventario(inventario): Muestra todos los productos del
inventario con su código, descripción y precio.
* buscar_producto(inventario, codigo): Busca un producto por su código.
Si existe, muestra su descripción y precio.
* modificar_precio(inventario, codigo, nuevo_precio): Modifica el precio
de un producto dado su código.
* eliminar_producto(inventario, codigo): Elimina un producto del
inventario usando su código.
* productos_por_rango_de_precio(inventario, min_precio, max_precio):
Muestra todos los productos cuyo precio esté entre min_precio y
max_precio.
"""

inventario = {
        "A001": ("Libro1", 23000),
        "A002": ("Celular", 150000),
        "A003": ("Mate", 7500),
        "A004": ("Funda", 11000),
        "A005": ("Llave", 9500)
}

def mostrar_inventario(inv):
    for key in inv:
        print(f"Codigo: {key}, Descripcion: {inv[key][0]}, Precio: ${inv[key][1]}")

def buscar_producto(inv, codigo):
    if codigo in inv:
        print(f"Producto encontrado: {inv[codigo][0]}, Precio: {inv[codigo][1]}")
    else:
        print("Producto NO encontrado.")

def modificar_precio(inv, codigo, nuevo):
    try:
        inv[codigo] = (inv[codigo][0],nuevo)
        print(f"El precio del producto con codigo {codigo} ha sido actualizado a ${nuevo}")
    except:
        print(f"No se pudo actualizar el precio del producto selectionado.")

def eliminar_producto(inv, codigo):
    try:
        inv.pop(codigo)
        print(f"El precio del producto con codigo {codigo} ha sido eliminado del inventario.")
    except:
        print(f"No se pudo eliminar el producto selectionado.")

def productos_por_rango_de_precios(inv, mini, maxi):
    for key in inv:
        if (mini <= inv[key][1] <= maxi):
            print(f"Codigo: {key}, Descripcion: {inv[key][0]}, Precio: ${inv[key][1]}")

while True:
    print("Opciones: demo, mostrar, buscar, modificar, eliminar, rango, exit")
    solicitado = input("Ingrese una solicitud: ")
    match solicitado:
        case "demo":
            print("mostar_inventario(inventario)")
            mostrar_inventario(inventario)
            print("-"*80)
            print("buscar_producto(inventario, 'A003')")
            buscar_producto(inventario, 'A003')
            print("-"*80)
            print("modificar_precio(inventario, 'A004', 6000)")
            modificar_precio(inventario, 'A004', 6000)
            print("-"*80)
            print("eliminar_producto(inventario, 'A002')")
            eliminar_producto(inventario, "A002")
            print("-"*80)
            print("productos_por_rango_de_precio(inventario, 10000, 100000)")
            productos_por_rango_de_precios(inventario, 10000, 100000)
        case "mostrar":
            mostar_inventario(inventario)
        case "buscar":
            cod = input("ingrese codigo: ")
            buscar_producto(inventario, cod)
        case "modificar":
            cod = input("ingrese codigo: ")
            nuevo = input("ingrese precio nuevo: ")
            modificar_precio(inventario, cod, nuevo)
        case "eliminar":
            cod = input("ingrese codigo: ")
            eliminar_producto(inventario, cod)
        case "rango":
            mini = input("ingrese min: ")
            maxi = input("ingrese precio nuevo: ")
            productos_por_rango_de_precios(inventario, mini, maxi)
        case "exit":
            break
