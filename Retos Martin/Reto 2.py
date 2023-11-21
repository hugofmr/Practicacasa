'''
Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
'''
# Inicio = int(input ('Indica numero inicial: '))
numero_inicial: int = 2

# fin= int('Indicame el numero final: ')
numero_final: int = 8

for i in range (numero_inicial, numero_final+1):
    if i%2 != 0:
        print(i)

