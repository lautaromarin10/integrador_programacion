from productos import productos

def busqueda_lineal(nombre_buscado: str):
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            return producto
    return None

def busqueda_binaria(nombre_buscado: str):
    productos_ordenados = sorted(productos, key=lambda x: x["nombre"].lower())
    izquierda = 0
    derecha = len(productos_ordenados) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = productos_ordenados[medio]["nombre"].lower()

        if actual == nombre_buscado.lower():
            return productos_ordenados[medio]
        elif nombre_buscado.lower() < actual:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return None

def buscar_por_nombre():
    nombre = input("Ingresa el nombre exacto del producto: ")
    metodo = int(input("Seleccioná el método de búsqueda:\n1) Búsqueda Lineal\n2) Búsqueda Binaria (requiere lista ordenada)\n"))

    if metodo == 1:
        resultado = busqueda_lineal(nombre)
    elif metodo == 2:
        resultado = busqueda_binaria(nombre)
    else:
        print("No ingresaste el nombre correcto")
        return buscar_por_nombre()

    if resultado:
        print("Tu producto:")
        print(resultado)
    else:
        print("Producto no encontrado.")

buscar_por_nombre()