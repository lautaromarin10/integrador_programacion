from productos import productos
import time

def quick_sort(productos: list):

    #Si la lista tiene 1 elemento o menos ya se encuentra ordenada
    if len(productos) <= 1:
        return productos

    #Se toma el elemento del medio como pivote
    pivote = productos.pop(len(productos) // 2)
    
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

    #Si la lista tiene 1 elemento o menos ya se encuentra ordenada
    if len(productos) < 1:
        return productos

    #Se divide la lista de productos en dos mitades.
    primer_lista = productos[:len(productos)//2]
    segunda_lista = productos[len(productos)//2:]

    #Ordenamos de forma recursiva cada mitad
    primer_lista = merge_sort(primer_lista)
    segunda_lista = merge_sort(segunda_lista)

    return merge(primer_lista, segunda_lista)

def nombre_algoritmo(algoritmo_seleccionado: int):
    #Retorna el nombre del algoritmo elegido en base a el numero ingresado por el usuario
    return "Quick Sort" if algoritmo_seleccionado == 1 else "Merge Sort"

def ejecutar_algoritmo_seleccionado(algoritmo: int):
    #Ejecuta el algoritmo seleccionado por el usuario
    return quick_sort(productos) if algoritmo == 1 else merge_sort(productos)

def ordenamiento_por_precio():

    #Se pide al usuario que eliga el algoritmo de ordenamiendo que desee utilizar
    algoritmo_elegido = int(input("Seleccione el algoritmo elegido para ordenar los productos por precio\n 1) Algoritmo Quick Sort\n 2) Algoritmo Merge Sort\n"))

    #Si el valor ingresado por el usuario no corresponde a un algoritmo, se vuelve a ejecutar de forma recursiva ordenamiento_por_precio
    if algoritmo_elegido not in [1,2]:
        print("El valor ingresado no corresponde a uno de los dos algoritmos disponibles, por favor intentalo nuevamente")
        ordenamiento_por_precio()
    
    #Se procede a calcular ei tiempo inicial, ejecutar el algoritmo y posteriormente tomar el tiempo que tardo en ejecutarse
    tiempo_inicial = time.time()
    print(ejecutar_algoritmo_seleccionado(algoritmo_elegido))
    tiempo_final = time.time()
    
    #Se imprime el tiempo de ejecución del algoritmo
    print(f"El Tiempo final de ejecución de {nombre_algoritmo(algoritmo_elegido)}: {tiempo_final - tiempo_inicial}")

ordenamiento_por_precio()