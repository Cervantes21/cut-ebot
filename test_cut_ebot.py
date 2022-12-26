class Mochilas():
    def __init__(self,numero,color,tipo,material):
        self.color = color
        self.numero = numero
        self.tipo = tipo
        self.material = material
        
    def mochilas(tipo):
        respuesta = (f'Necesitas {numero*4} de palas y {numero*2} tirantes color:{color}')
        print(respuesta)
class Loncheras():
    def __init__(self,numero,color):
        pass

class Cartucheras():
    def __init__(self,numero,color):
       pass
    
def choose_category(opcion):
    if opcion == 1:
        print('1. Mochilas')
    elif opcion == 2:
        print('2. Loncheras')
    elif opcion == 3:
        print('3. Cartucheras')
    else:
        print('Opcion no valida')



def choose_number():
    numero = int(input('* Cuantas Mochilas: '))

def choose_color():
    color = str(input('* Digite un color: '))

def choose_material():
    pass

def run():
    pass

if __name__ == '_main_':
    run()
    
opcion = int(input(f'Escoge una categoria \n 1. mochilas \n 2. loncheras \n 3. cartucheras \n'))
choose_category(opcion)
if choose_category(opcion=1):
    print(input('Escoge un tipo de Mochila: \n 1. Mochila Labastida \n 2. Mochila Laptop \n 3. Mochila Mark'))
elif choose_category(opcion=2):
    print(input('Escoge un tipo de Lonchera: \n 1. Lonchera Labastida \n 2. Lonchera Redonda \n 3. Lonchera beauty'))
elif choose_category(opcion=3):
    print(input('Escoge un tipo de Cartuchera: \n 1.Cartuchera mini-beuty \n 2. Cartuchera Sierra \n 3. Cartuchera cilindro'))
else:
    print('Opción no valida')