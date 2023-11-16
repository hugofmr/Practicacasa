productos = []
descuento_total = 0

opcion_escogida = ''

while opcion_escogida != 'X':
    opcion_escogida = input('''
Hola, escoge una opcion
1. Introducir Producto 
2. Obtener Ticket Final                                                                     
X. Salir del programa     

''')

    if opcion_escogida == '1':
        nombre_producto = input('Indica el nombre del producto: ')
        print(f'Has escogido: {nombre_producto}')

        precio_producto = float(input('Indica el precio del producto: '))
        print(f'Has indicado que el precio es: {precio_producto}')

        cantidad_producto = int(input('Indica la cantidad de producto: '))
        print(f'Has indicado que las unidades de producto son: {cantidad_producto}')

        descuento_producto = input('¿El producto cuenta con descuento? (S/N): ')
        if descuento_producto == 'S':
            descuento_producto_si = float(input('¿Cuánto es el porcentaje del descuento del producto?: '))
            descuento = precio_producto * (descuento_producto_si / 100)
        elif descuento_producto == 'N':
            descuento = 0
        else:
            print('Opción no válida. Introduce (S/N)')

            # Si no hay un 'continue', el código continuará ejecutándose
        total_producto = (precio_producto - descuento) * cantidad_producto
        productos.append({'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto, 'descuento': descuento, 'total': total_producto})
        descuento_total += descuento

    elif opcion_escogida == '2':
        if not productos:
            print('No hay productos para generar un ticket.')
        else:
            total_ticket = sum(producto['total'] for producto in productos)
            print('--- Ticket Final ---')
            for producto in productos:
                print(f"{producto['nombre']}: {producto['precio']} x {producto['cantidad']} = {producto['total']} con descuento de {producto['descuento']}")
            print(f"Descuento total: {descuento_total}")
            print(f"Total a pagar: {total_ticket - descuento_total}")
            print('---------------------')

    elif opcion_escogida != 'X':
        print('Opción no válida. Introduce una opción válida.')

print('¡Gracias por usar el programa!')
