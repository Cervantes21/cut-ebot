def run():

    poblacion_paises = {
        "Argentina": 44938712,
        "Brasil" : 210147125,
        "Colombia" : 50372425,
    }

    # print(poblacion_paises["Argentina"])

    # for pais in poblacion_paises.keys():
    #     print(pais)
    
    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")

if __name__ == "__main__":
    run()



# def run():
#     my_dict = {i: i**0.5 for i in range(1, 1001)}
#     print(my_dict)


# if __name__ == '__main__':
#     run()