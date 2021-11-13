#código para escribir los numeros del 1 al 100
contador = 1
print(contador)
while contador < 100:
    contador = contador + 1
    print(contador)

def con():
    contador = 0
    print(contador)
    while contador < 10:
        contador = contador + 1
        print(contador)
con()

for contador in range(1, 101):
    print(contador)
#con este código de arriba lo que hacemos es imprimir del número 1 hasta el 100
for i in range(11):
    print(8* i)
#con este código de arriba lo que hacemos es imprimir la tabla del 8 hasta que multiplique 8*10, de tal manera
#que para la variable i en el rango del 0 al 10 vamos a imprimir en cada vuelta del ciclo 11 por el valor de 
#la variable i, en este caso i primero ale 0 luego 1, 2, 3 hasta llegar al 10 y obtener 8*10 = 80
