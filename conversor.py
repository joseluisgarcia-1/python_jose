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
moneda = int(input("Ingresa los pesos colombianos que quieres cambiar a dólares: "))
valor_dolar = int(input("Ingresa el valor del dolar: "))
def colombia(moneda, valor_dolar):
    total_dolares = moneda/valor_dolar
    print("Los dolares que tienes es: ", total_dolares)
#valor_dolar = 3879
colombia(moneda, valor_dolar)