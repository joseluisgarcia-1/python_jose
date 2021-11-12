def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos "+ tipo_pesos +" tienes?: "))
    dolares = pesos/valor_dolar
    dolares_round = round(dolares, 2)
    dolares_caracteres = str(dolares_round)
    print("Tienes $", dolares_round, "dólares")
menu = """ Bienvenidos al mejor conversor de monedas, las opciones que hay a continuación las podemos seleccionar ingresando
su correspondiente número
1- Pesos colombianos
2- Pesos mexicanos
3- Pesos argentinos
4- Pesos bolivianos
 """

print(menu)
opcion = int(input("Ingresa tu opción: "))
print("Escogiste la opcion", opcion)

if opcion == 1:
    conversor("colombianos", 3879)
elif opcion == 2:
    conversor("mexicanos", 24)
elif opcion == 3:
    conversor("argentinos", 65)
elif opcion == 4:
    conversor("bolivianos", 7)
else:
    print("Elige una opción válida")

""""lo que entendí de esto hasta el momento es que, el conversor con los parametros recibe el tipo de pesos o de nacionalidad y el parametro
valor dolar es el valor del cada dolar en cada nacionalidad o moneda, por ejemplo en la opcion uno tenemos que, en la moneda de los colombianos
cada dolar cuesta 3879 pesos, por esta razón decimos que ingrese cuantos pesos tiene para dividir esos pesos de la nacionalidad, entre el valor
del dolar de cada nacionalidad correspondiente"""

