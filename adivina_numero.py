import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_ingresado = int(input("Ingresa un número para adivinar: "))
    while numero_ingresado != numero_aleatorio:
        if numero_ingresado < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_ingresado = int(input("Ingresa un nuevo número: "))
    print("Ganaste!!!!!, el número era el", numero_ingresado)
    

if __name__ == '__main__':
    run()