"""Escribe una aplicación con una variable que contenga una contraseña cualquiera.
Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
ha bloqueado después de los 3 intentos”. Fin programa."""

intentos = 0
password = "1234"

while intentos < 3:
    print((intentos + 1) , "° intento")
    passwordIngresada = input("Ingrese su contraseña")
    if passwordIngresada == password:
        print("Acceso correcto")
        break
    intentos += 1
if intentos > 2:
    print("El acceso ha sido bloqueado después de los 3 intentos")
