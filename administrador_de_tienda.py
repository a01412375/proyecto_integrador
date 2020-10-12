# administrador_de_tienda.py
#
# Jorge Claudio González Becerril
# Juan Daniel
# 10/2020

# Definición de funciones generales


def pedir_entero(num_min, num_max, peticion=''):
    ''' Regresa un entero cuando se encuentra entre dos rangos especificados. '''

    while True:
        # Solo acepta números enteros
        try:
            numero = int(input(f"\n{peticion} >> "))
        except:
            print("Ingrese un número válido.")
            continue

        # Solo acepta números entre los rangos establecidos
        if num_min <= numero <= num_max:
            return numero
        else:
            print("Ingrese un número valido.")


def pedir_eleccion(matriz, tipo_de_columna, peticion):
    ''' Muestra al usuario una lista de opciones y regresa su eleccion en un entero. '''

    # Obtiene la lista de opciones a desplegar
    lista = obtener_columna(matriz, tipo_de_columna)
    cantidad_lista = len(lista)
    mostrar_lista_en_menu(lista)

    eleccion = pedir_entero(1, cantidad_lista, f"{peticion} (1-{cantidad_lista})")

    return eleccion


def pasar_texto_a_matriz(nombre_texto):
    ''' Regresa una matriz apartir de un archivo de texto. '''

    matriz = []
    texto = open(nombre_texto, "r")

    for linea in texto:
        # Ignora los comentarios
        if linea[0] == "#":
            continue

        linea = linea.replace("\n", "")
        matriz.append(linea.split(","))

    texto.close()

    return matriz


def elegir_fila(matriz, num_fila):
    ''' Regresa una lista con la columna seleccionada de una matriz. '''

    return matriz[num_fila - 1]


def elegir_columna(matriz, num_columna):
    ''' Regresa una lista con la fila seleccionada de una matriz. '''

    lista = []

    for fila in matriz:
        lista.append(fila[num_columna - 1])

    return lista


def mostrar_lista_en_menu(lista):
    ''' Muestra al usuario una lista de todos los vendedores. '''

    print('')
    i = 1
    for nombre in lista:
        print(f"{i}) {nombre}")
        i += 1


def obtener_columna(matriz, tipo_de_columna):
    ''' Regresa una lista de la columna de un archivo de texto. '''

    matriz = elegir_columna(matriz, tipo_de_columna)

    return matriz


def editar_matriz_suma(matriz, fila, columna, valor_a_sumar):
    ''' Regresa una matriz con un valor alterado por una suma. '''

    matriz[fila][columna] = str(int(matriz[fila][columna]) + valor_a_sumar)


# Definición de funciones específicas


def mostrar_menu():
    ''' Muestra al usuario el menú principal del programa. '''

    print(f"\n1) Registrar ventas\n"
          f"2) Registrar llegada de artículos al almacén\n"
          f"3) Consultar datos del inventario\n"
          f"4) Consultar datos de las ventas\n"
          f"5) Mostrar reportes de ventas por vendedor\n"
          f"6) Mostrar reportes de ventas por artículo")


def mostrar_menu_registrar_ventas():
    '''
    Despliega el menú 1.
    Permite a un vendedor registar la venta de un producto por su parte.
    '''

    eleccion_vendedor = pedir_eleccion(matriz_vendedores, columnas_vendedores.get("nombre"), "Seleccione su nombre")
    id_vendedor = eleccion_vendedor - 1

    eleccion_producto = pedir_eleccion(matriz_productos, columnas_productos.get("nombre"),
                                       "Seleccione el producto a vender")
    id_producto = eleccion_producto - 1

    # Obtiene la cantidad disponible del producto
    cantidad = obtener_columna(matriz_productos, columnas_productos.get("cantidad"))
    cantidad_producto = int(cantidad[id_producto])

    # Avisa si el producto se encuentra agotado
    if cantidad_producto < 1:
        print("\nEl producto se encuentra agotado.")
        input("Da click para continuar.")
        return

    eleccion_cantidad = pedir_entero(1, cantidad_producto, f"Cantidad del producto a vender (1-{cantidad_producto})")

    # Actualiza los cambios realizados a las matrices
    editar_matriz_suma(matriz_ventas, id_vendedor, id_producto + 1, eleccion_cantidad)
    editar_matriz_suma(matriz_productos, id_producto, columnas_productos.get("cantidad") - 1, -eleccion_cantidad)


def obtener_diccionario_columnas_ventas():
    ''' Regresa un diccionario de las columnas en el archivo de texto de ventas. '''

    diccionario = {"id": 1}
    texto_ventas = open("ventas.txt", "r")
    linea = texto_ventas.readline()
    texto_ventas.close()

    linea = linea.split(",")

    for i in range(len(linea) - 1):
        diccionario[f"producto {i + 1}"] = i + 2

    return diccionario


# Declaración de diccionarios

columnas_productos = {"id": 1, "modelo": 2, "nombre": 3, "cantidad": 4}
columnas_vendedores = {"id": 1, "nombre": 2}
columnas_ventas = obtener_diccionario_columnas_ventas()  # {"id": 1, "producto 1": 2, ..., "producto n": n + 1}

# Declaración de matrices

matriz_productos = pasar_texto_a_matriz("productos.txt")
matriz_vendedores = pasar_texto_a_matriz("vendedores.txt")
matriz_ventas = pasar_texto_a_matriz("ventas.txt")

# Main

print("Bienvenido al Administrador de Tienda")

while True:
    mostrar_menu()
    eleccion = pedir_entero(1, 6, "Seleccione un menú (1-6)")

    if eleccion == 1:
        mostrar_menu_registrar_ventas()
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
