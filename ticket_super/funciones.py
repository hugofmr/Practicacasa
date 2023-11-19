

productos= []
total_general = 0
opcion_escogida = ''

# Función utilizada para el ingreso de los productos
def ingreso_producto():

    nombre_producto = input('Introduzca el nombre del producto: ')
    print(f'Has escogido: {nombre_producto}')

    precio_producto = float(input('Intruduzca el precio del producto: '))
    print(f'Has indicado que el precio es: {precio_producto}')

    cantidad_producto = int(input('Ingrese la cantidad de producto: '))
    print(f'Has indicado que las unidades de producto son: {cantidad_producto}')

    descuento_producto = input('¿El Producto tiene descuento?: si/no: ').lower()

    if descuento_producto == 'si':
        descuento = float(input('Ingrece el porcentaje del descuento: '))

    else:
        descuento = 0.0

    subtotal_producto = precio_producto * cantidad_producto - ( precio_producto * descuento * cantidad_producto / 100)
    total_descontado = round((cantidad_producto*precio_producto  ) - subtotal_producto,2)

    producto = {
        'nombre': nombre_producto,
        'precio': precio_producto,
        'cantidad': cantidad_producto,
        'descuento': descuento,
        'descontado': total_descontado,
        'subtotal': subtotal_producto
    }

    productos.append(producto)


while(opcion_escogida != 'X'):
    opcion_escogida= input('''
Hola, escoge una opcion
1. Introducir Producto 
2. Obtener Ticket Final                                                                     
X. Salir del programa     

        
''')
    # Para ingresar producto
    if (opcion_escogida == '1'):

        ingreso_producto()

    # Para imprimir el ticket
    elif (opcion_escogida == '2'):
        total_general = 0

        print('''
        ******************** Ticket de Compra ************************''')
        print(f"{'PRODUCTO':<15}| {'PRECIO':<10}| {'CANTIDAD':<10}| {'% DESCUENTO':<10}| {'DESCONTADO':<10}| {'SUBTOTAL':<10}")
        
        for producto in productos:
            print(f"{producto['nombre']:<14} | {producto['precio']:<10} | {producto['cantidad']:<10} | {producto['descuento']:<10} | {producto['descontado']:<10} |{producto['subtotal']:<10}")

            total_general += producto['subtotal']
        
        print(f'Total:                                                            {total_general}')


    

    # Para salir del programa
    elif (opcion_escogida.upper() == 'X'):
        print('Saliendo del programa.....')
        break

    else:
        print('Opcion no valida, por favor introduce: 1, 2 o X')





