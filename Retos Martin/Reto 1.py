'''
Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro del archivo main.py crea variables que representen los siguientes datos de un contacto:

Nombre
Apellidos
Edad
Email
Teléfono
Casado (verdadero o falso)
Con Hijos (verdadero o falso)
Lista de amigos
Películas vistas (diccionario con clave y valor. El valor será el título de la película)

Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
'''

nombre = "Hugo"
apellidos = "Maria Rodriguez"
edad = 31
telefono = "70297949"
casado = False
hijo = False
lista_de_amigos = ["Andre", "Erwin", "Velkeo", "Andy"]
peliculas_vistas = {
    "lunes": "Pulp Fiction",
    "martes": "Scar Face",
    "miercoles": "The Shining",
    "jueves": "God Father",
    "viernes": "Interestellar",
    "sabado": "Inception",
    "domingo": "Gladiator"
}

print(f'El día Lunes el usuario {nombre} {apellidos} de {edad}, con número de teléfono {telefono} ha visto {peliculas_vistas["lunes"]} con {lista_de_amigos[2]}')
print(f'El estado civil de {nombre} {apellidos} es {"casado" if casado else "soltero" } ')
print(f'El usuario {nombre} {apellidos} {"hijo" if hijo else "no tiene hijo"} ')
      