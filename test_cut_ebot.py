import os
class Category():
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
        print('Elegiste: Mochilas')
    elif opcion == 2:
        print('Elegiste: Loncheras')
    elif opcion == 3:
        print('Elegiste: Cartucheras')
    else:
        print('Opcion no valida')
    
    return opcion

def choose_type(opcion):
    opcion=choose_category(opcion)
    if opcion==1:
        print(input('Escoge un tipo de Mochila: \n 1. Mochila Labastida \n 2. Mochila Laptop \n 3. Mochila Mark \n'))
    elif opcion==2:
        print(input('Escoge un tipo de Lonchera: \n 1. Lonchera Labastida \n 2. Lonchera Redonda \n 3. Lonchera beauty \n'))
    elif opcion==3:
        print(input('Escoge un tipo de Cartuchera: \n 1.Cartuchera mini-beuty \n 2. Cartuchera Sierra \n 3. Cartuchera cilindro \n'))
    else:
        print('Opción no valida')
    return opcion
    
def choose_number(numero):
    numero = int(input('* ¿Cuántas piezas necesitas?: '))


def choose_color(color):
    color = str(input('* Digite un color: '))
    return color

def choose_material(tipo):
    tipo=choose_category(opcion)
    os.system('clear')
    print('* Elige un material: \n')
    if tipo==1:
        print(input('1. Poliester 600 \n 2. Poliester 1200 \n 3. Coreano \n 4. Mini-Ribstone \n'))
    elif tipo==2:
        print(input('1. Poliester 600 \n 2. Poliester 1200 \n 3. Coreano \n 4. Curpiel \n'))
    elif tipo==3:
        print(input('1. Poliester 600 \n 2. Curpiel \n 3. Coreano \n 4. B-30 \n'))
    return tipo

def run():
    pass

if __name__ == '_main_':
    run()
    
opcion = int(input(f'Escoge una categoria \n 1. mochilas \n 2. loncheras \n 3. cartucheras \n'))
choose_category(opcion)
os.system('clear')
choose_type(opcion)
os.system('clear')
choose_number(input)
choose_color(input)
choose_material(input)