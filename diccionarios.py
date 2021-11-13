def run():
    mi_dict = {
        1 : 'Messi', 2: 'Ronaldo', 3: 'Mbappe', 4:'Neymar'
    }
    print(mi_dict[1])
    print(mi_dict[2])
    print("****************")
    mi_dict2 = {
        'Psg': 'Francia', 'Madrid': 'España', 'City': 'Inglaterra'
    }
    print(mi_dict2['Psg'])
    print(mi_dict2['Madrid'])
    
    mi_dict3 = {
        'Moto': 'Yamaha', 'Carro': 1, 'Casas': 2 
    }
    print("****************")
    print(mi_dict3['Moto'])
    print(mi_dict3['Carro'])
    print(mi_dict3['Casas'])
    print("*****************")
    dict4 = {
        'Cauca': 'Popayán', 
        'Valle': 'Cali',
        'Putumayo': 'Mocoa',
        'Antioquia': 'Medellín'
    }
    #con el siguiente for imprimimos las llave del diccionario
    for i in dict4.keys():
        print(i)
    print("***************")
    #con el siguiente for imprimimos las llave del diccionario
    for i in dict4.values():
        print(i)
    print("***********")
    #con el siguiente for imprimimos las llave y los valores del diccionario
    for departamento, i in dict4.items():
        print("de", departamento, i, "es la capital")

if __name__ == '__main__':
    run()