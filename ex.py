productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0]
}

def stock_marca(marca):
    total = 0
    for clave, valor in productos.items():
        if (valor[0].lower() == marca.lower()):
            total +=stock[clave][1]
    print(f"El stock total de {marca} es: {total}")

def busqueda_precio(p_min,p_max):
    lista = []
    for clave, valor in stock.items():
        if (valor[0] > p_min and valor[0] < p_max and valor[1] > 0):
            lista.append(f"{productos[clave][0]}--{clave}")
    if (lista == []):
        print("No hay notebooks en ese rango de precios.”")
    else:
        lista.sort()
        print(f"Los notebooks entre los precios consulta son: {lista}")
    

def ordenar_productos():
    conteo = 0
    print("---------LISTADO DE PRODUCTOS ORDENADOS--------")
    for clave, valor in stock.items():
        if (valor[1] > 0):
            print (f"{productos[clave][0]} - {clave} - {productos[clave][2]} - {productos[clave][4]}")
        
        

def main ():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        opc = int(input("Por favor, ingrese una opcion: "))

        if (opc == 1):
            marca = input("Por favor, ingrese una marca: ")
            stock_marca(marca)
        elif (opc == 2):

            while True:
                try:
                    p_min = int(input("Por favor, ingrese el precio minimo: "))
                    p_max = int(input("Por favor, ingrese el precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

            busqueda_precio(p_min,p_max)
        elif (opc == 3):
            ordenar_productos()
        elif (opc == 4):
            print("Programa finalizado.")
            break
        else:
            print("Debe ingresar una opcion valida!!")


if __name__ == "__main__":
    main ()
