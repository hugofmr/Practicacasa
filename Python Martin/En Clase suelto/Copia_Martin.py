# Condicionales

# IF - ELIF (elif es opcional) - ELSE (else es opcional)

edad = 18

if (edad < 18):
  print('Menor de edad')
elif (edad >= 18 and edad < 40):
  print('Adulto Joven')
elif (edad >= 18 and edad < 70):
  print('Adulto')
else:
  print('Persona Mayor')

# BUCLES

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
        "producto": "Lechuga",
        "precio": 10.00,
        "unidades": 1,
        "descuento": 20
    },
]

# Bucle FOR para ITERAR por la lista y
# hacer un sumatorio de los precios de cada elemento y sacar el total de la cesta
# de la compra

print('''
******************** Ticket de Compra ************************''')
print(f"{'PRODUCTO':<10}| {'PRECIO':<10}| {'UNIDADES':<10}| {'DESCUENTO':<10}| {'TOTAL':<10}")
precio_total = 0
for elemento in lista_compra:
  precio_total_elemento = 0
  descuento_aplicado = 0
  producto = elemento["producto"]
  precio_elemento = elemento["precio"]
  unidades = elemento["unidades"]
  porcentaje_descuento = elemento["descuento"]


  if (porcentaje_descuento != 0):
    # Aplicamos el descuento
    descuento_aplicado = precio_elemento * (porcentaje_descuento / 100)
    precio_despues_del_descuento = precio_elemento - descuento_aplicado
    precio_total_elemento = precio_despues_del_descuento * unidades
    
    
    print('descuento_aplicado', descuento_aplicado)
  else:
    precio_total_elemento = precio_elemento * unidades
  
  precio_total += precio_total_elemento
  

  
  if(descuento_aplicado != 0):
    print(
        f'{producto:<15}{precio_elemento:<12}{unidades:<10} {descuento_aplicado:<10} {precio_total_elemento:<10}'
    )
  else:
    print(
        f'{producto:<15}{precio_elemento:<12}{unidades:<10} {"-":<10} {precio_total_elemento:<10}'
    )

# Salimos del bucle y ya tenemos el precio_total actualizado
print(f'''
--------------------------------------------------------------
Total:                                                 {precio_total}€
''')


'''
#Bucles While 

lista = [1,2,3,4,5,6,7,8]

# Bucle WHILE para encontrar eliminar elementos hasta que la longitud sea 3
while (len(lista) > 3):
    lista.pop()
    print(lista)

'''