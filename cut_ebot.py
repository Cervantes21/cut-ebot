class categorias (mochilas, loncheras, cartucheras):
    mochilas = [m_labastida, m_blair, m_kipling]
    loncheras = [mini_beauty, l_labastida, l_redonda]
    cartucheras = [c_beauty_fa, c_circular, c_american]
    
    def mochilas(numero, color):
        m_labastida = 0
        m_blair = 0
        m_kipling = 0
        
    def loncheras(numero, color):
        mini_beauty = 0
        l_labastida = 0
        l_redonda = 0
    
    def cartucheras(numero, color):
        c_beauty_fa = 0
        c_circular = 0
        c_american = 0
        
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

def run():
    pass


if __name__ == "__main__":
    run()