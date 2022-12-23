def categoria(opcion):
    opcion = int(input(f'Escoge una categoria \n 1. mochilas \n 2. loncheras \n 3. cartucheras \n'))

    if opcion == 1:
        print('1. Mochilas')
    elif opcion == 2:
        print('2. Loncheras')
    elif opcion == 3:
        print('3. Cartucheras')
    else:
        print('Opcion no valida')

    def n_pzas(opcion,numero):
        if opcion== 1:
            numero = int(input('* Cuantas mochilas: '))
        elif opcion==2:
            numero = int(input('* Cuantas loncheras: '))
        elif opcion==3:
            numero = int(input('* Cuantas Cartucheras: '))
        else:
            print('Opcion no valida')
        return numero

    def choose_color(color):
        colors = [
            'Azul',
            'Rojo',
            'A. Marino',
            'Negro',
            'Guinda',
            'Amarillo'
        ]
        for c in colors:
            print(c)
        color = str(input('* Digite un color: '))
        return color

def choose_material(material):
    pass
def run():
    pass

if __name__ == '_main_':
    run()
