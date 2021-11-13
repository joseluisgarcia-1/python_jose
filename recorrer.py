def run():
    """nombre = str(input("Ingresa un nombre: "))
    for i in nombre:
        print(i)"""
    
    frase = str(input("Escribe una cadena de caracteres: "))
    for i in frase:
        print(i.lower())
    
"""con esto recorremos la palabra dada letra por letra por medio de un for"""
if __name__ == '__main__':
    run()