def run():
    pass
def mochilas(numero,color):
    numero = int()
    color = str()
    
def loncheras(numero,color):
    numero = int()
    color = str()
def cartucheras(numero, color):
    numero = int()
    color = str()
opcion = int(input(f'Escoge una categoria \n 1. mochilas \n 2. loncheras \n 3. cartucheras \n'))

if opcion == 1:
    print('1. Mochilas')
    numero = int(input('* Cuantas Mochilas: '))
    color = str(input('* Digite un color: '))
    mochilas(numero,color)
    respuesta = (f'Necesitas {numero*4} de palas y {numero*2} tirantes color:{color}')
    print(respuesta)
    
elif opcion == 2:
    print('2. Loncheras')
    numero = int(input('* Cuantas Loncheras: '))
    color = str(input('* Digite un color: '))
    loncheras(numero,color)
    respuesta = (f'Necesitas {numero*2} de palas y {numero*4} fuelles color:{color}')
    print(respuesta)
elif opcion == 3:
    print('3. Cartucheras')
    numero = int(input('* Cuantas Cartucheras: '))
    color = str(input('Digite un color: '))
    cartucheras(numero,color)
    respuesta = (f'Necesitas {numero*2} de palas y {numero*2} fuelles color:{color}')
    print(respuesta)
else:
    print('Opcion no valida')




if __name__ == '_main_':
    run()
