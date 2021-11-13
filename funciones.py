"""def conversation(mensaje):
    print("Hola")
    print("Samara")
    print(mensaje)
    print("Estás hermosa")
"""
def conversation(hola):
    print("Hola")
    print("Samara")
    print(hola)
    print("Estás hermosa")
opcion = int(input("Ingresa un número de opción: "))

if opcion == 1:
    conversation("Elegiste la opcion 1")
elif opcion == 2:
    conversation("Elegiste la opción 2")
elif opcion == 3:
    conversation("Elegiste la opcion 3")
elif opcion == 4:
    conversation("Elegiste la opcion 4")
elif opcion == 5:
    conversation(hola=2)
elif opcion == 6:
    conversation(hola="Nuevo mensaje amigo")
#se debe tener en cuenta que la función recibe el parametro mensje
#sirve
#elif opcion == 4:
#    conversation(mensaje="Hola amiguito")
#sirve
#elif opcion == 4:
#    conversation(mensaje= 1)
else:
    print("Escribe una opción válida")