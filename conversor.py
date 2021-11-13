#esto sirve
"""pesos_colombianos = int(input("¿Ingresas los pesos colombianos que quieres cambiar a dólares?"))
valor_dolar = 3879
total_dolares = pesos_colombianos/valor_dolar
dolares_caracteres = str(total_dolares)
print(dolares_caracteres)
print(type(dolares_caracteres))"""

"""#esta sirve solo que es cuando uno tiene un menú pues escoger la opcion y luego pasarle los datos
opcion = int(input("Ingresa el número de opción de la moneda que quieres convertir: "))
print("Escogiste la opcion", opcion)
if opcion == 1:
    moneda = int(input("Ingresa los pesos colombianos que quieres cambiar a dólares: "))
    valor_dolar = int(input("Ingresa el valor del dolar: "))
    def colombia(moneda, valor_dolar):
        total_dolares = moneda/valor_dolar
        print("Los dolares que tienes es: ", total_dolares)
    #valor_dolar = 3879
    colombia(moneda, valor_dolar)
if opcion != 1:
    print("opcion no valida")
"""
#esta tambien sirve, solo que esta es como para calcular datos para una sola opcion
"""moneda = int(input("Ingresa los pesos colombianos que quieres cambiar a dólares: "))
valor_dolar = int(input("Ingresa el valor del dolar: "))
def colombia(moneda, valor_dolar):
    total_dolares = moneda/valor_dolar
    dolares_totales = round(total_dolares, 2)
    print("Los dolares que tienes es: ", dolares_totales)
#valor_dolar = 3879
colombia(moneda, valor_dolar)"""

menu = """ Bienvenidos al mejor conversor de monedas, las opciones que hay a continuación las podemos seleccionar ingresando
su correspondiente número
1- Pesos colombianos a dolares
2- Dolares a pesos colombianos
3- Pesos mexicanos a colombianos
4- Pesos colombianos a mexicanos
 """
print(menu)
opcion = int(input("Ingresa tu opción: "))
print("Escogiste la opcion", opcion)
precio_dolar = 3879
precio_mexicano = float(187.54)
if opcion == 1:
    print("El precio del dolar está en:",precio_dolar)
    colombianos = int(input("Ingresa el valor de pesos colombianos: "))
    def colombianos_dolares(colombianos):
        total_dolares = colombianos/precio_dolar
        dolares_total = round(total_dolares, 2)
        print("Los dolares que tienes es:",dolares_total)
    colombianos_dolares(colombianos)
elif opcion == 2:
    print("El precio del dolar está en:",precio_dolar)
    dolares = int(input("Ingresa el valor de dolares que quieres pasar a pesos colombianos: "))
    def colombianos_dolares(dolares):
        total_dolares = precio_dolar*dolares
        dolares_total = round(total_dolares, 2)
        print("Los dolares que tienes es:",dolares_total)
    colombianos_dolares(dolares)
elif opcion == 3:
    print("El precio del peso mexicano está en:",precio_mexicano)
    mexicanos = int(input("Ingresa el valor de pesos mexicanos que quieres convertir: "))
    def mexicanos_colombianos(mexicanos):
        total_mexicanos = mexicanos*precio_mexicano
        mexicanos_total = round(total_mexicanos, 2)
        print("Los pesos mexicanos que tienes es:",mexicanos_total)
    mexicanos_colombianos(mexicanos)
elif opcion == 4:
    print("El precio del peso mexicano está en:",precio_mexicano)
    colombianos = int(input("Ingresa el valor de pesos colombianos: "))
    def colombianos_mexicanos(colombianos):
        total_colombianos = colombianos/precio_mexicano
        colombianos_total = round(total_colombianos, 2)
        print("Los pesos colombianos que tienes es:",colombianos_total)
    colombianos_mexicanos(colombianos)
else:
    print("Ingresa una opción valida, porque la opción que ingresaste que es la", opcion,"no está dentro del menú")