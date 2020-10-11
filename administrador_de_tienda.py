# administrador_de_tienda.py
#
# Jorge Claudio González Becerril
# Juan Daniel
# 10/2020

# Definición de funciones


def pedir_entero(num_min, num_max, peticion=''):
    ''' Regresa un entero cuando se encuentra entre dos rangos especificados. '''

    while True:
        # Solo acepta números enteros
        try:
            numero = int(input(f"{peticion} >> "))
        except:
            print("Ingrese un número válido.")
            continue

        # Solo acepta números entre los rangos establecidos
        if num_min <= numero <= num_max:
            return numero
        else:
            print("Ingrese un número valido.")


def pasar_texto_a_matriz(texto):
    ''' Regresa una matriz apartir de un archivo de texto. '''

    matriz = []

    for linea in texto:
        # Ignora los comentarios
        if linea[0] == "#":
            continue

        linea = linea.replace("\n", "")
        matriz.append(linea.split(","))

    return matriz


def elegir_columna(matriz, columna):
    pass


def mostrar_menu():
    ''' Muestra al usuario el menú principal del programa. '''

    print(f"1) Registrar ventas\n"
          f"2) Registrar llegada de artículos al almacén\n"
          f"3) Consultar datos del inventario\n"
          f"4) Consultar datos de las ventas\n"
          f"5) Mostrar reportes de ventas por vendedor\n"
          f"6) Mostrar reportes de ventas por artículo")


def menu_registrar_ventas():
    ''' Despliega el menú 1. '''
    pass    # Muestra la lista de vendedores
    pass    # pedir_entero(1, numero de vendedores)


def mostrar_vendedores():
    ''' Muestra al usuario una lista de todos los vendedores. '''

    lista_vendedores = open("vendedores.txt", "r")

    for linea in lista_vendedores:
        if linea[0] == "#":
            continue



# Declaración de variables

pass

# Main

while True:
    mostrar_menu()
    eleccion = pedir_entero(1, 6, "Seleccione un menú (1-6)")

    if eleccion == 1:
        pass
    elif eleccion == 2:
        pass
    elif eleccion == 3:
        pass
    elif eleccion == 4:
        pass
    elif eleccion == 5:
        pass
    elif eleccion == 6:
        pass
