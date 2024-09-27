"""
Cada producto: codigo, descripcion, precio.
"""
def mostarInventario (produc):
    for codigo, (descripcion, precio) in produc.items():
      print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")

def buscarProducto (produc, produc3):
    if produc3 in produc:
       descripcion, precio = produc[produc3]
       print(f"Producto encontrado: {descripcion}, Precio: ${precio}")

def modificarPrecio(produc, cod, num):
   if cod in produc:
    descripcion, _ = produc[cod]
    produc[cod] = (descripcion, num)
    print(f"El precio del producto {descripcion} ha sido actualizado a ${num}.")

def eliminarProducto (produc, cod):
   produc.pop(cod)
   print("El producto con código", cod, "ha sido eliminado del inventario")

productos = {
    "A001": ("Pantalon", 15000),
    "A002": ("Remera", 20000),
    "A003": ("Campera", 50000),
    "A004": ("Buzo", 50000),
    "A005": ("Medias", 5000),
}

mostarInventario(productos)
print("")
buscarProducto(productos, "A003")
print("")
modificarPrecio(productos, "A004", 60000)
print("")
eliminarProducto(productos, "A002")