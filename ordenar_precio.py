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