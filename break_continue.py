def run():
    """for contador in range(49):
        if contador % 2 != 0:
            continue
        print(contador)"""
    """si hay un número en ese rango de numeros y el contador al dividirlo por 2 el resto es distinto a 0, 
    voy a saltarme esta vuelta del ciclo y voy a ejecutar continue es decir imprima el contador y con ello tenemos 
    el dato"""
    """palabra = str(input("Escribe una palabra: "))
    for i in palabra:
        if i == 'h':
            continue
        print(i)
    """
    """si el ciclo encuentra una letra h dentro de la palabra dada ejecute el continue"""
    palabra = str(input("Escribe una palabra: "))
    for i in palabra:
        if i == 'h':
            break
        print(i)
    """si el ciclo encuentra una letra h dentro de la palabra dada ejecute el break"""

if __name__ == '__main__':
    run()