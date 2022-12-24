def Mochilas (objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
    

def Loncheras (objetivo, epsilon):
    paso = epsilon**2
    respuesta = 0.0
    iteraciones = 0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        iteraciones += 1

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def Cartucheras (objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    # absoluto = abs(respuesta**2 - objetivo)
    # print(f'absoluto: {absoluto}')

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2   

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')  

opcion = int(input(f'Escoge una categoria \n 1. Mochilas \n 2. Loncheras \n 3. Cartucheras \n'))

if opcion == 1:
    print('1. Mochilas')
    numero = int(input('* Digite un numero: '))
    Mochilas(numero)
elif opcion == 2:
    print('2. Loncheras')
    numero = int(input('* Digite un numero: '))
    parametro_epsilon = float(input('* Digite un epsilon: '))
    Loncheras(numero,parametro_epsilon)
elif opcion == 3:
    print('3. Cartucheras')
    numero = int(input('* Digite un numero: '))
    parametro_epsilon = float(input('* Digite un epsilon: '))
    Cartucheras(numero,parametro_epsilon)
else:
    print('Opcion no valida')
    
# Imprimimos el menú en pantalla
print("""
    1) Herramientas       3) Temperatura
    2) Calculadora        4) Mas...
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona algo :")

# Según lo que ingresó, código diferente
if eligio=="1":
    print("Listamos otras herramientas")
elif eligio=="2":
    x = 3
    y = 5
    print("x * y = ", x * y)
elif eligio=="3":
    print("Creo que hace frío")
elif eligio=="4":
    print("otra opción")
else:
    print("Opción no válida")