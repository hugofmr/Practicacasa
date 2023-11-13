
#Creando alumno 1

alumno1 = {
    "nombre": "Hugo",
    "email": "hugo@email.com",
    "curso": [
      {
        "nombre": "Fundamentos de Python",
        "examenes": [
                {
                    "nombre": "Examen Python",
                    "duracion": 1.3,
                    "nota": 6
                },
                {
                    "nombre": "Examen Loop",
                    "duracion": 1.5,
                    "nota": 8
                }
        ]
      }
    ]         
}

alumno2= {
    "nombre": "Pepe",
    "email": "pepe@email.com",
    "cursos": [
        {
            "nombre": "Fundamentos de Linux",
            "examenes": [
                {
                    "nombre": "Examen de Terminal",
                    "duracion": 2.4,
                    "nota": 7            
                },
                {
                    "nombre": "Examen de Comandos",
                    "duracion": 3.5,
                    "nota": 10
                }
            ]            
        },
        {
            "nombre": "Python Intermedio",
            "examenes": [
                {
                    "nombre": "Examen de Condicionales",
                    "duracion": 4.2,
                    "nota": 8                    
                },
                {
                    "nombre": "Examen de Loop",
                    "duracion": 4.1,
                    "nota": 4
                }
            ]
        }        
    ]
}

lista_master = []

lista_master.append(alumno1)
lista_master.append(alumno2)

print(f'- Alumno1: { lista_master[0]} ')

# 1. Obtener el nombre del alumno 1 desde la lista.

print(f'El nombre del alumno 1 es: { alumno1["nombre"] }')

# 2. Obtener la nota del segundo examen del segundo curso del alumno2 en la lista.

print(f'La nota del examen Loop del alumno2 es: { alumno2["cursos"][1]["examenes"][1]["nota"] }')