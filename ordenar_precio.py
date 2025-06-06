from productos import productos

def quick_sort(productos: list):

    #Se selecciona el ultimo producto como Pivote
    pivote = productos.pop()
    
    #Se declara las listas de precios
    precio_alto = []
    precio_bajo = []

    #Se recorre la lista de productos y con un ternario evaluamos el precio
    #precio_alto: Se agrega a la lista si el precio del producto actual es mayor al precio del pivote
    #precio_bajo: Se agrega a la lista si el precio del producto actual es mas bajo que el precio del pivote
   
    for producto in productos:
        precio_alto.append(producto) if producto["precio"] >= pivote["precio"] else precio_bajo.append(producto)

    #Se concatena todos las listas de precios utilizando recursivamente quick sort junto con el pivote
    return quick_sort(precio_bajo) + [pivote] + quick_sort(precio_alto)

def merge(primer_lista : list, segunda_lista : list):
    resultado = []
    indice = [0,0] #indice de primera y segunda lista

    while indice[0] < len(primer_lista) and indice[1] < len(segunda_lista):
        if primer_lista[indice[0]]["precio"] < segunda_lista[indice[1]]["precio"]:
            resultado.append(primer_lista[indice[0]])
            indice[0] += 1
        else:
            resultado.append(segunda_lista[indice[1]])
            indice[1] += 1

    # Verificar elementos restantes en la primer lista
    while indice[0] < len(primer_lista):
        resultado.append(primer_lista[indice[0]])
        indice[0] += 1
    
    # Verificar elementos restantes en la segunda lista
    while indice[1] < len(segunda_lista):
        resultado.append(segunda_lista[indice[1]])
        indice[1] += 1
    
    return resultado


def merge_sort(productos: list):

    if len(productos) < 2:
        return productos

    primer_lista = productos[:len(productos)//2]
    segunda_lista = productos[len(productos)//2:]

    #Ordenamos de forma recursiva cada mitad
    primer_lista = merge_sort(primer_lista)
    segunda_lista = merge_sort(segunda_lista)

    return merge(primer_lista, segunda_lista)
