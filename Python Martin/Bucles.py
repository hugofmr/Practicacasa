#Bucles

lista_compra = [
    {
        "producto": "Leche",
        "precio": 2.00,
        "unidades": 6,
        "descuento": 0
    },
    {
        "producto": "Patatas",
        "precio": 5.00,
        "unidades": 10,
        "descuento": 0
    },
    {
        "producto": "lechuga",
        "precio": 4.00,
        "unidades": 1,
        "descuento": 2
    }
]


# Bucle FOR para iterar por lista y hacer un sumatorio de los precios de cada elemento 
# y sacar el total de la cesta de compra

'''
print('Precios de la compra')
for elemento in lista_compra:
    #print(elemento) #esto se ejecuta tantas veces haya elementos en esa lista.
    print (f'- {elemento["precio"]}€')
'''

# mostrar por consola el precio de la total lista de la compra 
# variable de precio total en la que suma los precios individuales

'''
print ('***** Ticket Final *****')

precio_total = 0
for elemento in lista_compra:
    precio_total += elemento["precio"]

# Salimos del bucle y ya tenemos el precio_total actualizado

print(f'Precio Total: {precio_total} €')
'''
'''
# calcular precio total a partir de cuantas unidades tenemos de cada elemento

print ('***** Ticket Final *****')

precio_total = 0
for elemento in lista_compra:
    unidades = elemento ["unidades"]
    precio_elemento = elemento ["precio"]
    precio_total_elemento = precio_elemento * unidades
    precio_total += precio_total_elemento

# Salimos del bucle y ya tenemos el precio_total actualizado
print(f'Precio Total: {precio_total}€')
'''

# Creando el formato de ticket de compra

print('******************* Ticket de Compra ****************')
#print('Producto | Precio (€) | Unidades | Descuento | Total')
print(f"{'PRODUCTO':<10}| {'PRECIO (€)':<10}| {'UNIDADES':<10}| {'DESCUENTO':<10}| {'TOTAL':<10}|")
precio_total= 0

for elemento in lista_compra:
    precio_total_elemento = 0
    descuento_aplicado = 0
    producto = elemento["producto"]
    precio_elemento= elemento ["precio"]
    unidades = elemento ["unidades"]
    descuento= elemento["descuento"]

    if (descuento != 0):
        #aplicamos el descuento
        precio_con_descuento = precio_elemento * (descuento / 100)
        precio_total_elemento = precio_con_descuento * unidades
    else:
        precio_total_elemento = precio_elemento * unidades


    precio_total_elemento = precio_elemento * unidades
    precio_total += precio_total_elemento
    print(f'{producto:<15}{precio_elemento:<15}{unidades:<10}{"-"}{precio_total_elemento:<15}')
    



#Salimos del bucle

print(f'''--------------------------------------------------
      Total:                                                     Precio Total: {precio_total}€
      
      
      ''')