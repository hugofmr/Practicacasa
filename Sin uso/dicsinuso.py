data = [{
    'area': 'area1',
    'Equipo': 'equipo1',
    'precio': 1 
},
{
    'area': 'area2',
    'Equipo': 'equipo3',
    'precio': 5
},
{
    'area': 'area3',
    'Equipo': 'equipo3',
    'precio': 4 
}
]

# Inicializar la variable de suma
suma_precios = 0

# Iterar sobre cada diccionario en la lista
for elemento in data:
    # Sumar el precio de cada elemento al total
    suma_precios += elemento['precio']

# Imprimir la suma de precios
print(f"La suma de todos los precios es: {suma_precios}")