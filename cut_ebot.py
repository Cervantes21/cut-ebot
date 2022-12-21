def run():
    pass
def mochilas():
    numero = ()
    color = ()
    respuesta = opcion
def loncheras():
    pass
def cartucheras():
    pass

opcion = int(input(f'Escoge una categoria \n 1. mochilas \n 2. loncheras \n 3. cartucheras \n'))

if opcion == 1:
    print('1. Mochilas')
    numero = int(input('* Cuantas mochilas: '))
    color = str(input('* Digite un color: '))
    mochilas(numero,color)
elif opcion == 2:
    print('2. Loncheras')
    numero = int(input('* Cuantas mochilas: '))
    color = str(input('* Digite un color: '))
    loncheras(numero,color)
elif opcion == 3:
    print('3. Cartucheras')
    numero = int(input('* Cuantas mochilas: '))
    color = str(input('Digite un color: '))
    Cartucheras(numero,color)
else:
    print('Opcion no valida')




if __name__ == '_main_':
    run()
