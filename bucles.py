def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: #mientras potencia de 2 sea menor qué límite
        print("2 elevado a " + str(contador) + "es igual a: " + str(potencia_2))#esto se imprime siempre y cuando se cumpla lo de arriba
        contador = contador + 1 # ahora al contador le decimos que vale 1
        potencia_2 = 2**contador # y a la potencia le ponemos que sume la siguiente potencia

#y así se hace el ciclo
    
if __name__ == '__main__':
    run()