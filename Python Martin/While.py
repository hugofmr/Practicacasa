opcion_escogida= ''

while(opcion_escogida != 'X'):
    opcion_escogida= input('''
Hola, escoge una opcion
1. Introducir Producto 
2. Obtener Ticket Final                                                                     
X. Salir del programa     

        
''')
    if (opcion_escogida == '1'):
        nombre_producto: str = input('Indica el nombre del producto')
        print(f'Has escogido: {nombre_producto}')
        precio_producto: float = input ('Indica el precio del producto')
        print(f'Has indicado que el precio es: {precio_producto}')
        cantidad_producto: int = input('indica la cantidad de producto')
        print(f'Has indicado que las unidades de producto son: {cantidad_producto}')
        descuento_producto: input('¿el producto cuenta con descuento?(S/N)')
            if descuento_producto == 'S':
                descuento_producto_si: int = input ('¿cuanto es el portaje del descuento del producto?')
            else (descuento_producto == 'N')
                descuento_producto_no = 0

        

    #elif(opcion_escogida == '2')