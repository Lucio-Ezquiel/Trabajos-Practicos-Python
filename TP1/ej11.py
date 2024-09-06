"""
11) Escribe una aplicación con una variable que contenga una contraseña cualquiera.
Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
ha bloqueado después de los 3 intentos”. Fin programa.
"""
password = "HelloWorld1"
intentos = 1
while True:
    entered = input("Ingrese la contraseña: ")
    if entered == password:
        print("Acceso Correcto")
        break
    elif intentos == 3:
        print("El acceso se ha bloqueado despues de los 3 intentos.")
        break
    intentos += 1


