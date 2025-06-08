from productos import productos

def filtrar_por_categoria(categoria_buscada: str):
    return [producto for producto in productos if producto["categoria"].lower() == categoria_buscada.lower()]

def ejecutar_filtrado_categoria():
    categoria = input("Ingresá la categoría: ")
    resultados = filtrar_por_categoria(categoria)

    if resultados:
        print(f"\nProductos en la categoría '{categoria}':\n")
        for producto in resultados:
            print(producto)
    else:
        print(f"No se encontraron productos en la categoría '{categoria}'.")

ejecutar_filtrado_categoria()