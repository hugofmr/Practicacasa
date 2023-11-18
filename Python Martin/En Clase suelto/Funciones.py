# Declarando funciones para utilizar por nosotros mismos
# ejemplo crear una similar a .upper()

# mostrar saludo () # no se pueden ejecutar o llamar funciones no declaradas previamente, el orden importa
#Declaracion de funciones sin parametros
def mostrar_salududo():
    print('Hola Martin')

# Llamada y ejecucion a funciones sin parametro
mostrar_salududo() #para llamar a una funcion y ejecutarla es necesario ponerle parentesis al final.


# Funciones con parametros(con tipos o sin tipos)

def mostar_despedida(nombre: str, apellidos: str):
    nombre_completo = f'{nombre} {apellidos}'
    print(f'Hasta la vista Sr. {nombre_completo}')

# Llamada y ejecuciones de funciones con parametros
mostar_despedida('Hugo', 'Maria') # El orden por defecto
mostar_despedida(nombre='Hugo', apellidos='Maria') # Especificar el parametro y al reves seria el parametro desordenado
mostar_despedida(apellidos='Maria', nombre='Hugo') # Especificar el parametro desordenado


# Funciones con parametro por defecto

def saludar_mundo(publico: str= 'Mundo'):
    print(f'Hola, {publico}, ¿Como estas?')

saludar_mundo()  # Hola mundo
saludar_mundo('clase')


#Funciones con retorno

def saludar_sin_espacios(nombre: str, apellidos: str) -> str:
    #Primero eliminar los caracteres en blanco del nombre y apellido, tanto delante como detras    
    nombre_completo = f'{nombre.strip()} {apellidos.strip()}'
    return nombre_completo #devuelve un texto

nombre_sin_espacios = saludar_sin_espacios(' Hugo ', ' Maria ')

print(f'Hola, {nombre_sin_espacios}')

# Funcion dentro de otra funcion

def imprimir_saludo_sin_espacios(nombre: str, apellidos: str) -> str:
    #Primero eliminar los caracteres en blanco del nombre y apellido, tanto delante como detras    
    nombre_completo = f'{nombre.strip()} {apellidos.strip()}'
    saludar_mundo(nombre_completo)

imprimir_saludo_sin_espacios(' Hugo ', ' Maria ')










