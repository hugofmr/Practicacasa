descuento_total = 0 #Almacenta deascuento para calculo previo
productos = []
descuento= 0 #Almacena los descuentos si es que hay alguna aplicacion
total_general= 0 #Variable para almacenar el general total para la suma a pie de pagina 

opcion_escogida= ''

while(opcion_escogida != 'X'):
    opcion_escogida= input('''
Hola, escoge una opcion
1. Introducir Producto 
2. Obtener Ticket Final                                                                     
X. Salir del programa     

        
''')
    if (opcion_escogida == '1'):

        nombre_producto = input('Indica el nombre del producto: ')
        print(f'Has escogido: {nombre_producto}')

        precio_producto = float(input ('Indica el precio del producto: '))
        print(f'Has indicado que el precio es: {precio_producto}')

        cantidad_producto = int(input('indica la cantidad de producto: '))
        print(f'Has indicado que las unidades de producto son: {cantidad_producto}')

        descuento_producto= input('¿El producto cuenta con descuento?(S/N): ')
        if (descuento_producto.upper() == 'S'):
            descuento_producto_si = float(input ('¿cuanto es el portaje del descuento del producto?: '))
            descuento = round(precio_producto * (descuento_producto_si / 100),2) #redondeando resultado a 2 decimales
        elif (descuento_producto.upper() == 'N'):
            descuento = 0
        else:
            print('Opcion no valida. Introduce (S/N)')
            

        total_producto = round(( precio_producto - descuento) * cantidad_producto, 2)
        productos.append({'nombre': nombre_producto, 'precio': precio_producto, 'cantidad': cantidad_producto, '% Dcto': descuento_producto_si, 'descuento': descuento, 'total': total_producto})
        descuento_total += descuento
        #total_general += productos['total']
        #total_general = int(sum(productos['total'] for total_producto in productos))     
        
    elif (opcion_escogida == '2'):
        print('''
        ******************** Ticket de Compra ************************''')
        print(f"{'PRODUCTO':<15}| {'PRECIO':<10}| {'CANTIDAD':<10}| {'% Dcto':<10}| {'DESCUENTO':<10}| {'TOTAL':<10}")
        print(f"{productos['nombre']:<14} | {productos['precio']:<10} | {productos['cantidad']:<10} | {productos['% Dcto']:<10} | {productos['descuento']:<10} | {productos['total']:<10}")


        for producto in productos:
            print(f"{producto['nombre']:<14} | {producto['precio']:<10} | {producto['cantidad']:<10} | {producto['% Dcto']:<10} | {producto['descuento']:<10} | {producto['total']:<10}")
           
        
        
               
        print('''
        --------------------------------------------------------------
        Total:                                                 {total_general}€
        ''')
    elif (opcion_escogida.upper() == 'X'):
        print('Saliendo del programa.....')
        break

    else:
        print('Opcion no valida, por favor introduce: 1, 2 o X')
        