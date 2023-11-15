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
        print