Categorias = [loncheras, cartucheras, mochilas]

loncheras = [mini_beauty, lonchera_labastida, lonchera_redonda]

mini_beuty = [2, palas_mb, 1, f_arrastre_mb, 2, f_cierre_mb]
palas_mb = int[(27) (17)]
f_arrastre_mb = int[(50.2) (12.2)]
f_cierre_mb = int[(30.2) (6)]

lonchera_labastida = [2 palas_ll, 1 f_arrastre_ll, 2 f_cierre_ll 2 cartera_ll, 2 tirantes_ll)]
palas_ll = 27.5 "x" 22
f_arrastre_ll = 52.2 "x" 22
f_cierre_ll = 46 "x" 7.4
cartera_ll = 22 "x" 18.5
tirantes_ll = 38 "x" 11.3

lonchera_redonda

cartucheras = [cartuchera_beauty_fa, cartuchera_circular, cartuchera_american]
mochilas = [m_labastida, m_blair, m_kipling]
print(mini_beuty)
# =======

# >>>>>>> 7ab2fed9a5ce4adad9aac90b9393073f163084ac
# >>> modelo = input("Cual modelo quieres: ")
# Cual modelo quieres: labastida
# >>> modelo
# 'labastida'
# >>> print("Elegiste: ", modelo, " es correcto?")
# Elegiste:  labastida  es correcto?
# >>> print(f"Elegiste {modelo} es correcto?")
# Elegiste labastida es correcto?
# >>> print(f"Elegiste: {modelo} es correcto?")
# Elegiste: labastida es correcto?
# >>> cantidad = int(input("Cuántas mochilas quieres: "))
# estudiantes = {
#     'mexico': 10,
#     'colombia': 15,
#     'puerto_rico': 4,
# }

# for pais in estudiantes:
#     ...

# for pais in estudiantes.keys():
#     ...

# for numero_de_estudiantes in estudiantes.values():
#     ...

# for pais, numero_de_estudiantes in estudiantes.items():
#     ...

class categorias (mochilas, loncheras, cartucheras):
    mochilas = [m_labastida, m_blair, m_kipling]
    loncheras = [mini_beauty, l_labastida, l_redonda]
    cartucheras = [c_beauty_fa, c_circular, c_american]
    
    def mochilas(numero):
        m_labastida = 0
        m_blair = 0
        m_kipling = 0
        
    def loncheras(numero):
        mini_beauty = 0
        l_labastida = 0
        l_redonda = 0
    
    def cartucheras(numero):
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